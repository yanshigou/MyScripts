# -*- coding: utf-8 -*-
__author__ = 'dzt'
__date__ = '2018/10/22 21:58'

from django import forms


class ImeiInfoForm(forms.Form):
    info = forms.CharField(label=u'文件备注', min_length=1)
    filename = forms.FileField(label=u'上传文件')


class LoginForm(forms.Form):
    username = forms.CharField(required=True)
    password = forms.CharField(required=True, min_length=5)