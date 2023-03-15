from django.shortcuts import render
from tasks.serializers import TaskSerializer
from tasks.models import Task
from rest_framework import generics, mixins
from rest_framework.permissions import IsAuthenticated
from django.db.models import Q


class TaskListView(
    mixins.CreateModelMixin, mixins.ListModelMixin, generics.GenericAPIView
):
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Task.objects.filter(Q(owner=user) | Q(assignees=user))

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class TaskDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]
