# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.views.generic.base import View
import xlrd

from datetime import datetime
from django.http import HttpResponse
from forms import ImeiInfoForm, FileInfoForm
from models import FileInfo, ImeiInfo

# Create your views here.
class WriteView(View):
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
            src = 'upload/%s' % file_name    # 连接成上传文件的路径
            rb = xlrd.open_workbook(filename=src)  # 打开文件
            sheet1 = rb.sheet_by_index(0)  # 通过索引获取表格
            print(sheet1.name)

            cols = sheet1.col_values(0)  # 获取列内容
            imeis = []
            ok_imeis = []
            error_imeis = []

            for col in cols:
                print col
                # if len(col)< 14:
                #     continue
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
                nowstate = 'ok'
            # 获取数据库数据
                imeiinfo = ImeiInfo()
                imeiinfo.imei = nowimei
                imeiinfo.state = nowstate
                imeiinfo.oktime = datetime.now()
                imeiinfo.filename = file_name
                imeiinfo.save()
                print(i)

            for x in error_imeis:

                nowimei = x
                nowstate = 'error'
                # 获取数据库数据
                imeiinfo = ImeiInfo()
                imeiinfo.imei = nowimei
                imeiinfo.state = nowstate
                imeiinfo.oktime = datetime.now()
                imeiinfo.filename = file_name
                imeiinfo.save()
            return HttpResponse('file upload ok !')

    def get(self, request):
        form = ImeiInfoForm()
        return render(request, 'writetodb.html', {'form':form})