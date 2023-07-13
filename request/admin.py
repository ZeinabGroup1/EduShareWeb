from django.contrib import admin
from .models import *


class RequestAdmin(admin.ModelAdmin):
    list_display = ('user', 'receiver', 'status', 'date', 'time')


admin.site.register(Request, RequestAdmin)
