# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from infra.models import Company, Slot
# Register your models here.

admin.site.register(Company)
admin.site.register(Slot)