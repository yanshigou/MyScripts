# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from models import PLL


class PLLAdmin(admin.ModelAdmin):
    list_display = ['task_id', 'info', 'filename', 'starttime', 'oktime', 'download']


admin.site.register(PLL, PLLAdmin)