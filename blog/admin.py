from django.contrib import admin
from .models import Blog


# Register your models here.
class BlogAdmin(admin.ModelAdmin):
    readonly_fields = ['date']


admin.site.register(Blog, BlogAdmin)


# admin.site.register(Blog)


# @admin.register(Comment)
# class CommentAdmin(admin.ModelAdmin):
#     list_display = ('name', 'email', 'post', 'created', 'active')
#     list_filter = ('active', 'created', 'updated')
#     search_fields = ('name', 'email', 'body')
#     actions = ['approve_comments']
#
#     def approve_comments(self, request, queryset):
#         queryset.update(active=True)
