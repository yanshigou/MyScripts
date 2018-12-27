# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import AbstractUser


class UserProfile(AbstractUser):
    nick_name = models.CharField(max_length=50, verbose_name=u'昵称', default='')
    company = models.CharField(max_length=100, default='', verbose_name=u'公司名称')
    mobile = models.CharField(max_length=11, null=True, blank=True)

    class Meta:
        verbose_name = '用户信息'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.username


class PLL(models.Model):
    task_id = models.CharField(max_length=128, null=True, blank=True, default='')
    info = models.CharField(max_length=30, verbose_name=u'备注', default='')
    count = models.IntegerField(verbose_name=u'数据量', null=True, blank=True)
    filename = models.FileField(upload_to='upload', verbose_name=u'文件名')
    starttime = models.DateTimeField(null=True, blank=True, verbose_name=u'开始时间')
    oktime = models.DateTimeField(null=True, blank=True, verbose_name=u'完成时间')
    download = models.FileField(upload_to='download', verbose_name=u'资源文件', max_length=100)



