from rest_framework import generics, mixins
from rest_framework.permissions import IsAuthenticated

from drf_api.permissions import IsOwnerOrReadOnly
from tasks.models import Task
from tasks.serializers import (
    TaskComment,
    TaskCommentSerializer,
    TaskSerializer,
)


class TaskListView(
    mixins.CreateModelMixin, mixins.ListModelMixin, generics.GenericAPIView
):
    """View for Tasks"""

    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        """Retrieve all tasks, ordered by updated_at"""
        return Task.objects.all().order_by("-updated_at")

    def get(self, request, *args, **kwargs):
        """Retrieve all tasks"""
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        """Creates a new task"""
        return self.create(request, *args, **kwargs)


class TaskDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    """View for retrieving, updating or deleting a task"""

    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]


class TaskCommentAPIView(generics.CreateAPIView):
    """View for creating a comment"""

    serializer_class = TaskCommentSerializer
    permission_classes = [IsAuthenticated]


class TaskCommentUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    """View for retrieving, updating or removing a task comment"""

    queryset = TaskComment.objects.all()
    serializer_class = TaskCommentSerializer
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]

    def get_queryset(self):
        """Retrieve all comments for a specific task"""
        queryset = super().get_queryset()
        task_pk = self.kwargs["task_pk"]
        return queryset.filter(task_id=task_pk).all()
