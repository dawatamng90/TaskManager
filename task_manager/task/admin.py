from django.contrib import admin
from .models import Task

@admin.action(description='Update completion status for selected tasks')
def update_status(modeladmin, request, queryset):
    for task in queryset:
        task.update_completion_status()

class TaskAdmin(admin.ModelAdmin):
    list_display = ('task_name', 'status', 'due_date', 'completed_date')
    actions = [update_status]

admin.site.register(Task, TaskAdmin)
