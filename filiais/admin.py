# -*- coding: utf-8 -*-

from django.contrib import admin
from .models import BranchLicense


class BranchModelsAdmin(admin.ModelAdmin):
    model = BranchLicense
admin.site.register(BranchLicense, BranchModelsAdmin)
