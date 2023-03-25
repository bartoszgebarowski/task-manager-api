from django.shortcuts import render
from tasks.serializers import (
    TaskSerializer,
    TaskCommentSerializer,
    TaskComment,
)
from tasks.models import Task
from rest_framework import generics, mixins
from rest_framework.permissions import IsAuthenticated

from drf_api.permissions import IsOwnerOrReadOnly


class TaskListView(
    mixins.CreateModelMixin, mixins.ListModelMixin, generics.GenericAPIView
):
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Task.objects.all().order_by("-updated_at")

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class TaskDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]


class TaskCommentAPIView(generics.CreateAPIView):
    serializer_class = TaskCommentSerializer
    # permission_classes = [IsAuthenticated]


class TaskCommentUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = TaskComment.objects.all()
    serializer_class = TaskCommentSerializer
    # permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]

    def get_queryset(self):
        queryset = super().get_queryset()
        task_pk = self.kwargs["task_pk"]
        return queryset.filter(task_id=task_pk).all()
