from django.urls import path
from tasks.views import TaskListView, TaskDetailAPIView

urlpatterns = [
    path("", TaskListView.as_view(), name="task_list"),
    path("<int:pk>", TaskDetailAPIView.as_view(), name="task_detail"),
]
