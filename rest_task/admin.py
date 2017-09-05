from django.contrib import admin
from rest_task import models as mymodels

# Register your models here.

class TaskAdmin(admin.ModelAdmin):
    search_fields = ['user', 'title', 'created_at', 'time_elapsed', 'status',
                     'is_complete']
    list_display = ['user', 'title', 'created_at', 'time_elapsed','status',
                    'is_complete']
admin.site.register(mymodels.Task, TaskAdmin)