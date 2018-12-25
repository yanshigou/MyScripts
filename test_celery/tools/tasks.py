# -*- coding: utf-8 -*-
from __future__ import absolute_import
from celery import shared_task
import time
import xlrd
import xlwt
from datetime import datetime
from paopao.models import PLL
import requests


SERVER_URL = "此URL上传文件在某个接口访问/查询/命令等的链接"


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
    error_imeis = []

    for col in cols:
        # print col
        # if len(col)< 14:
        #     continue
        if col == 'imei':
            continue
        imei = str(int(col))
        # print imei
        if len(imei) != 15:
            error_imeis.append(imei)
            continue
        else:
            ok_imeis.append(imei)
            data = {"imei": imei}
            try:
                res = requests.post(SERVER_URL, data=data)
                res.raise_for_status()
                error_no = res.json()["error_no"]
                if error_no == 0:
                    print("pao imei=" + imei)
                elif error_no == 4:
                    print("offline imei=" + imei)
                else:
                    print("error imei=" + imei)
            except:
                print("error imei=" + imei)

    f = xlwt.Workbook()
    sheet1 = f.add_sheet('validIMEI', cell_overwrite_ok=True)
    for i in range(0, len(ok_imeis)):
        sheet1.write(i, 0, str(ok_imeis[i]))

    sheet2 = f.add_sheet('invalidIMEI', cell_overwrite_ok=True)
    for i in range(0, len(error_imeis)):
        sheet2.write(i, 0, error_imeis[i])

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
    count = len(ok_imeis) + len(error_imeis)

    p = PLL.objects.get(starttime=time1)
    p.oktime = datetime.now()
    p.download = new_imei_file
    p.count = count
    p.save()
    return
