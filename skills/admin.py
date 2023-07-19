from django.contrib import admin
from .models import *


class SkillsAdmin(admin.ModelAdmin):
    list_display = ('user', 'category', 'title', 'time', 'rate', 'description')


admin.site.register(Skills, SkillsAdmin)
admin.site.register(SkillsCategory)
admin.site.register(SkillsTime)
