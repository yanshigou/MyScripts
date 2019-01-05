# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.views.generic.base import View
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse

from forms import ImeiInfoForm, LoginForm
from models import PLL, UserProfile
from tools.tasks import test_task, get_imei
from django.shortcuts import render_to_response
from tools.db import Db
from datetime import datetime
from tools.mixin_utils import LoginRequiredMixin
import os




from django.contrib.auth.backends import ModelBackend
from django.db.models import Q
from django.contrib.auth import authenticate, login


class Results(LoginRequiredMixin, View):
    def get(self, request):
        # 查询所有的任务信息
        db = Db()
        rows = db.get_tasksinfo()
        return render_to_response('results.html', {'rows': rows})


class Index(View):
    def get(self, request):
        return render(request, 'index.html')


class UploadView(LoginRequiredMixin, View):
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
            return HttpResponseRedirect('/uploaded/')

    def get(self, request):
        form = ImeiInfoForm()
        return render(request, 'upload.html', {'form': form})


class GetView(LoginRequiredMixin, View):
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
            result = get_imei.delay(time1)
            p = PLL.objects.get(starttime=time1)
            p.task_id = result.id
            p.save()
            return HttpResponseRedirect('/uploaded/')

    def get(self, request):
        form = ImeiInfoForm()
        return render(request, 'get.html', {'form': form})


class Download(LoginRequiredMixin, View):
    def get(self, request, file_name):
        # src = 'D:/dzt/Work_CMX/paoliuliang/celery_imei/test_celery/%s' % file_name
        src = '/home/ubuntu/www/cmxcelery/%s' % file_name
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


class CustomBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            user = UserProfile.objects.get(Q(username=username)|Q(email=username))
            if user.check_password(password):
                return user
        except Exception as e:
            return None


class LoginView(View):
    def get(self, request):
        return render(request, "login.html", {})

    def post(self, request):
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            user_name = request.POST.get('username', '')
            pass_word = request.POST.get('password', '')
            user = authenticate(username=user_name, password=pass_word)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponseRedirect('/')
                else:
                    return render(request, 'login.html', {'msg':"用户未激活"})
            else:
                return render(request, 'login.html', {'msg':'用户名或密码错误！'})
        else:
            return render(request, 'login.html', {'login_form':login_form})


class Uploaded(LoginRequiredMixin, View):
    def get(self, request):
        all = PLL.objects.all()
        return render(request, 'uploaded.html', {
            'all': all
        })


class DelFile(LoginRequiredMixin, View):
    def get(self, request, task_id):
        try:
            task = PLL.objects.get(task_id=task_id)
            filename = task.filename
            download = task.download
            task.delete()
            print(filename)
            print(download)
            # src_filename = 'D:\\dzt\\Work_CMX\\paoliuliang\\celery_imei\\test_celery\\upload\\%s' % filename
            # src_download = 'D:\\dzt\\Work_CMX\\paoliuliang\\celery_imei\\test_celery\\%s' % download
            src_filename = '/home/ubuntu/www/cmxcelery/upload/%s' % filename
            src_download = '/home/ubuntu/www/cmxcelery/%s' % download
            if os.path.exists(src_filename) and os.path.exists(src_download):
                os.remove(src_filename)
                os.remove(src_download)
                print('ok')
            else:
                print('notfind file')
            return HttpResponseRedirect('/results/')
        except:
            return HttpResponseRedirect('/results/')
