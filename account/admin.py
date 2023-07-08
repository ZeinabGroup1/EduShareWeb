from django.contrib import admin
from .models import *


class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'phone', 'first_name', 'last_name', 'country', 'city','complete')


admin.site.register(Profile,ProfileAdmin)
