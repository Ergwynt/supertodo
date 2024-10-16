from django.contrib import admin

from .models import Task


@admin.register(Task)
class Taskadmin(admin.ModelAdmin):
    list_display = ('slug', 'name', 'done', 'created_at')
    prepopulated_fields = {'slug': ['name']}
