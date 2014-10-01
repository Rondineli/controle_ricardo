# -*- coding: utf-8 -*-

from django.contrib import admin
from .models import ControlLicense


class LicensesModelsAdmin(admin.ModelAdmin):
    model = ControlLicense
admin.site.register(ControlLicense, LicensesModelsAdmin)
