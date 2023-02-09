from django.shortcuts import render
from tasks.serializers import TaskSerializer
from tasks.models import Task
from rest_framework import generics, mixins
from rest_framework.permissions import IsAuthenticated


class TaskListView(
    mixins.CreateModelMixin, mixins.ListModelMixin, generics.GenericAPIView
):
    serializer_class = TaskSerializer
    queryset = Task.objects.all()
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
