# -*- coding: utf-8 -*-
from __future__ import absolute_import
from celery import shared_task
import json
import xlrd
import xlwt
from datetime import datetime
from paopao.models import PLL
import requests
from django.db import connection
from time import sleep
from .email_send import send_register_email, listen_nginx


SERVER_URL = "http://ip地址/commander/paopao/"
GET_SERVER_URL = "http://ip地址/common/querydownload/?imei="
# SERVER_URL = "http://ip地址/smartlock/checkimei/"


@shared_task(track_started=True)
def test_task(time1):
    filename = PLL.objects.get(starttime=time1).filename
    print(filename)

    src = 'upload/%s' % filename  # 连接成上传文件的路径
    print(src)
    rb = xlrd.open_workbook(filename=src)  # 打开文件
    sheet1 = rb.sheet_by_index(0)  # 通过索引获取表格
    print(sheet1.name)

    cols = sheet1.col_values(0)  # 获取列内容
    ok_imeis = []
    offline_imeis = []

    for col in cols:
        # print col
        # if len(col)< 14:
        #     continue
        if col == 'imei':
            continue
        imei = str(int(col))
        # print imei
        if len(imei) != 15:
            continue
        else:
            data = {"imei": imei}
            try:
                res = requests.post(SERVER_URL, data=data)
                res.raise_for_status()
                error_no = res.json()["error_no"]
                if error_no == 0:
                    print("pao imei=" + imei)
                    ok_imeis.append(imei)
                elif error_no == 4:
                    print("offline imei=" + imei)
                    offline_imeis.append(imei)
                else:
                    print("error imei=" + imei)
            except:
                print("error imei=" + imei)

    f = xlwt.Workbook()
    sheet1 = f.add_sheet('success', cell_overwrite_ok=True)
    for i in range(0, len(ok_imeis)):
        sheet1.write(i, 0, str(ok_imeis[i]))

    sheet2 = f.add_sheet('fail', cell_overwrite_ok=True)
    for i in range(0, len(offline_imeis)):
        sheet2.write(i, 0, offline_imeis[i])

    print(filename)
    print(type(filename))

    filename = str(filename).split('/')[1]
    print(filename)

    if filename[-3:] == 'xls':
        new_imei_file = 'upload/download/paoliuliang_' + filename
    elif filename[-4:] == 'xlsx':
        new_imei_file = 'upload/download/paoliuliang_' + filename[:-1]
    else:
        new_imei_file = 'upload/download/paoliuliang_imei.xls'

    f.save(new_imei_file)
    count = len(ok_imeis) + len(offline_imeis)

    connection.close()
    sleep(10)

    p = PLL.objects.get(starttime=time1)
    p.oktime = datetime.now()
    p.download = new_imei_file
    p.count = count
    p.save()
    return


@shared_task(track_started=True)
def get_imei(time1):
    filename = PLL.objects.get(starttime=time1).filename
    print(filename)

    src = 'upload/%s' % filename  # 连接成上传文件的路径
    print(src)
    rb = xlrd.open_workbook(filename=src)  # 打开文件
    sheet1 = rb.sheet_by_index(0)  # 通过索引获取表格
    print(sheet1.name)

    cols = sheet1.col_values(0)  # 获取列内容
    ok_imeis = []
    no_imeis = []

    for col in cols:
        # print col
        # if len(col)< 14:
        #     continue
        if col == 'imei':
            continue
        imei = str(int(col))
        # print imei
        if len(imei) != 15:
            continue
        else:
            try:
                res = requests.get(url=GET_SERVER_URL+imei).content
                res = json.loads(res)
                print(res)
                exist = res.get('exist')
                if exist is False:
                    no_imeis.append(imei)
                    print(imei + "false")
                elif exist is True:
                    ok_imeis.append(imei)
                    print(imei + "true")
            except:
                print("error imei=" + imei)

    f = xlwt.Workbook()
    sheet1 = f.add_sheet('success_IMEI', cell_overwrite_ok=True)
    for i in range(0, len(ok_imeis)):
        sheet1.write(i, 0, str(ok_imeis[i]))
        sheet1.write(i, 1, "success")
    sheet2 = f.add_sheet('fail_IMEI', cell_overwrite_ok=True)
    for i in range(0, len(no_imeis)):
        sheet2.write(i, 0, no_imeis[i])
        sheet2.write(i, 1, "fail")

    print(filename)
    print(type(filename))

    filename = str(filename).split('/')[1]
    print(filename)

    if filename[-3:] == 'xls':
        new_imei_file = 'upload/download/result_' + filename
    elif filename[-4:] == 'xlsx':
        new_imei_file = 'upload/download/result_' + filename[:-1]
    else:
        new_imei_file = 'upload/download/result_imei.xls'

    f.save(new_imei_file)
    count = len(ok_imeis) + len(no_imeis)

    connection.close()
    sleep(10)

    p = PLL.objects.get(starttime=time1)
    p.oktime = datetime.now()
    p.download = new_imei_file
    p.count = count
    p.save()
    return


@shared_task(track_started=True)
def listen_ngx_celery():
    try:
        res = listen_nginx()
        if res.status_code != 200:
            print('not 200', datetime.now())
            send_register_email('dongzhetong@cmx-iot.com', res)
            # send_register_email('daijian@cmx-iot.com', res)
        else:
            print("is's ok", datetime.now())
    except Exception as e:
        print('Exception！', datetime.now())
        send_register_email('dongzhetong@cmx-iot.com', None, e)
        # send_register_email('daijian@cmx-iot.com', None, e)

