from django.urls import path
from tasks.views import (
    TaskListView,
    TaskDetailAPIView,
    TaskCommentAPIView,
    TaskCommentUpdateDestroyView,
)

urlpatterns = [
    path("", TaskListView.as_view(), name="task_list"),
    path("<int:pk>", TaskDetailAPIView.as_view(), name="task_detail"),
    path(
        "<int:task_pk>/comments",
        TaskCommentAPIView.as_view(),
        name="task_comments",
    ),
    path(
        "<int:task_pk>/comments/<int:pk>",
        TaskCommentUpdateDestroyView.as_view(),
        name="task_comments_detail",
    ),
]
