# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models


class PLL(models.Model):
    task_id = models.CharField(max_length=128, null=True, blank=True, default='')
    info = models.CharField(max_length=30, verbose_name=u'备注', default='')
    count = models.IntegerField(verbose_name=u'数据量', null=True, blank=True)
    filename = models.FileField(upload_to='upload', verbose_name=u'文件名')
    starttime = models.DateTimeField(null=True, blank=True, verbose_name=u'开始时间')
    oktime = models.DateTimeField(null=True, blank=True, verbose_name=u'完成时间')
    download = models.FileField(upload_to='download', verbose_name=u'资源文件', max_length=100)

