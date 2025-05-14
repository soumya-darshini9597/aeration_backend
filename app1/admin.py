from django.contrib import admin
from .models import Areation

@admin.register(Areation)
class AreationAdmin(admin.ModelAdmin):
    list_display = ['time','date','state']