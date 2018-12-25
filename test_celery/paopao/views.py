# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.views.generic.base import View
from django.http import HttpResponse

from forms import ImeiInfoForm
from models import PLL
from tools.tasks import test_task
from django.shortcuts import render_to_response
from tools.db import Db
from datetime import datetime


class Results(View):
    def get(self, request):
        # 查询所有的任务信息
        db = Db()
        rows = db.get_tasksinfo()
        return render_to_response('result.html', {'rows': rows})


class UploadView(View):
    def post(self, request):
        form = ImeiInfoForm(request.POST, request.FILES)
        if form.is_valid():
            # 获取表单数据
            info = form.cleaned_data['info']
            filename = form.cleaned_data['filename']
            time1 = datetime.now()

            f = PLL()
            f.filename = filename
            f.info = info
            f.starttime = time1
            f.save()

            print(filename)
            print(type(filename))
            print(str(filename))
            print(type(str(filename)))

            # 要注意 filename 为<class 'django.core.files.uploadedfile.InMemoryUploadedFile'>
            # 名字不能直接等于str(filename), 不然无法保存上传文件
            result = test_task.delay(time1)
            p = PLL.objects.get(starttime=time1)
            p.task_id = result.id
            p.save()
            return render(request, 'index.html', {})

    def get(self, request):
        form = ImeiInfoForm()
        return render(request, 'upload.html', {'form': form})


class Download(View):
    def get(self, request, file_name):
        src = 'D:/dzt/Work_CMX/paoliuliang/celery_imei/test_celery/%s' % file_name
        print(src)
        response = HttpResponse(readFile(src))
        response['Content-Type'] = 'application/octet-stream'
        response['Content-Disposition'] = 'attachment;filename="{0}"'.format(file_name)
        return response


def readFile(fn, buf_size=262144):  # 大文件下载，设定缓存大小
    f = open(fn, "rb")
    while True:  # 循环读取
        c = f.read(buf_size)
        if c:
            yield c
        else:
            break
    f.close()

