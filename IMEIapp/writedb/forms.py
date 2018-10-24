__author__ = 'dzt'
__date__ = '2018/10/22 21:58'

from django import forms


class FileInfoForm(forms.Form):
    username = forms.CharField()
    filename = forms.FileField()


class ImeiInfoForm(forms.Form):
    username = forms.CharField()
    filename = forms.FileField()