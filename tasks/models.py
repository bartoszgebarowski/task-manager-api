from django.db import models
from profiles.models import TaskManagerUser


class Task(models.Model):
    title = models.CharField(max_length=100)
    owner = models.ForeignKey(
        TaskManagerUser, on_delete=models.CASCADE, related_name="task_owner"
    )
    assignees = models.ManyToManyField(TaskManagerUser, blank=True)
    description = models.TextField(blank=True)
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(
        auto_now_add=True, editable=False, verbose_name="Created at"
    )
    updated_at = models.DateTimeField(
        auto_now=True, null=True, editable=False, verbose_name="Updated at"
    )

    def __str__(self):
        return f"{self.title}"
