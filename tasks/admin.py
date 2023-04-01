from django.contrib import admin

from tasks.models import Task, TaskComment

admin.site.register(Task)
admin.site.register(TaskComment)
