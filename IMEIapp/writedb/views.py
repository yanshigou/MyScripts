# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.views.generic.base import View
import xlrd
from rest_framework.views import APIView

from datetime import datetime
from django.http import HttpResponse, HttpResponseRedirect
from forms import ImeiInfoForm, FileInfoForm
from models import FileInfo, ImeiInfo, PLL
import requests
from pure_pagination import Paginator, EmptyPage, PageNotAnInteger


SERVER_URL = ""


class UploadView(View):
    def post(self, request):
        form = ImeiInfoForm(request.POST, request.FILES)
        if form.is_valid():
            # 获取表单数据
            username = form.cleaned_data['username']
            filename = form.cleaned_data['filename']

            #获取数据库数据
            file = FileInfo()
            file.username = username
            file.filename = filename
            file.save()

            file_name = FileInfo.objects.filter(filename__endswith='xlsx').order_by('-id')[0].filename
            print(file_name)


            url = '/run/%s' % file_name
            return HttpResponseRedirect(url)


    def get(self, request):
        form = ImeiInfoForm()
        return render(request, 'writetodb.html', {'form': form})


class Paoliuliang(View):
    def get(self, request, file_name):
        all = PLL.objects.filter(filename=file_name)
        # 分页
        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1

        p = Paginator(all, 20, request=request)

        all_imei = p.page(page)
        return render(request, 'index.html', {
            "all_imei": all_imei
        })


def paoliuliang(file_name):
    imeis = ImeiInfo.objects.filter(state='wait', filename=file_name).values('imei')
    print(imeis)
    for i in imeis:
        nowimei = i['imei']
        data = {"imei": nowimei}
        try:
            res = requests.post(SERVER_URL, data=data)
            res.raise_for_status()
            error_no = res.json()["error_no"]
            if error_no == 0:
                print("pao imei=" + nowimei)
                nowstate = 'success'
            elif error_no == 4:
                nowstate = 'offline'
                print("offline imei=" + nowimei)
            else:
                nowstate = 'error'
                print("error imei=" + nowimei)
        except:
            nowstate = 'error'
            print("error imei=" + nowimei)

        pao = PLL()
        pao.imei = nowimei
        pao.state = nowstate
        pao.oktime = datetime.now()
        pao.filename = file_name
        pao.save()

        imeiinfo = ImeiInfo.objects.get(imei=nowimei, state='wait', filename=file_name)
        imeiinfo.state = nowstate
        imeiinfo.oktime = datetime.now()
        imeiinfo.save()


class read_and_pao(APIView):
    def post(self, request):
        file_name = request.data.get('file_name')
        file_name = file_name.split('/')[3]
        print(file_name)
        time1 = datetime.now()
        src = 'upload/upload/%s' % file_name  # 连接成上传文件的路径
        rb = xlrd.open_workbook(filename=src)  # 打开文件
        sheet1 = rb.sheet_by_index(0)  # 通过索引获取表格
        print(sheet1.name)

        cols = sheet1.col_values(0)  # 获取列内容
        imeis = []
        ok_imeis = []
        error_imeis = []
        filename = 'upload/%s' % file_name

        for col in cols:
            print col
            # if len(col)< 14:
            #     continue
            if col == 'imei':
                continue
            imei = str(int(col))
            imeis.append(imei)
            # print imei
            if len(imei) != 15:
                error_imeis.append(imei)
            else:
                ok_imeis.append(imei)

        print('ok:', ok_imeis)
        print('error:', error_imeis)
        for i in ok_imeis:
            nowimei = i
            nowstate = 'wait'

            imeiinfo = ImeiInfo()
            imeiinfo.imei = nowimei
            imeiinfo.state = nowstate
            imeiinfo.filename = filename
            imeiinfo.save()

        for x in error_imeis:
            nowimei = x
            nowstate = 'error'

            imeiinfo = ImeiInfo()
            imeiinfo.imei = nowimei
            imeiinfo.state = nowstate
            imeiinfo.oktime = datetime.now()
            imeiinfo.filename = filename
            imeiinfo.save()

        paoliuliang(filename)
        time2 = datetime.now()
        times = str(time2 - time1)
        print('总共耗时：%s' % times)
        return HttpResponse("跑流量完成，耗时%s" % times)