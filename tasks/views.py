from django.shortcuts import render
from tasks.serializers import TaskSerializer
from tasks.models import Task
from rest_framework import generics

class TaskListView(generics.ListAPIView):
    serializer_class = TaskSerializer
    queryset = Task.objects.all()
    