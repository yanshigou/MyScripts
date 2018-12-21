# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from datetime import datetime
from django.db import models

# Create your models here.
class ImeiInfo(models.Model):
    imei = models.CharField(max_length=50)
    state = models.CharField(max_length=20, default='unfinished')
    starttime = models.DateTimeField(default=datetime.now)
    oktime = models.DateTimeField(null=True)
    filename = models.CharField(max_length=100)

    class Meta:
        unique_together = ("imei", "state")  # 联合唯一

    def __unicode__(self):
        return self.imei


class FileInfo(models.Model):
    username = models.CharField(max_length=30, verbose_name=u'上传用户名')
    filename = models.FileField(upload_to='upload', verbose_name=u'Excel文件')

    def __unicode__(self):
        return self.username


class PLL(models.Model):
    imei = models.CharField(max_length=50)
    state = models.CharField(max_length=20, default='unfinished')
    oktime = models.DateTimeField(null=True)
    filename = models.CharField(max_length=100)