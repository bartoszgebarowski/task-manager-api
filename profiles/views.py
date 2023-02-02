from rest_framework import generics
from profiles.serializers import TaskManagerUserSerializer


class CreateTaskManagerUserView(generics.CreateAPIView):
    serializer_class = TaskManagerUserSerializer
