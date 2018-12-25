# -*- coding: utf-8 -*-
__author__ = 'dzt'
__date__ = '2018/10/22 21:58'

from django import forms


class ImeiInfoForm(forms.Form):
    info = forms.CharField()
    filename = forms.FileField()
