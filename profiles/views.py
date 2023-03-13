from rest_framework import generics
from profiles.serializers import TaskManagerUserSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response


class CreateTaskManagerUserView(generics.CreateAPIView):
    serializer_class = TaskManagerUserSerializer


class UserDetailView(generics.RetrieveAPIView):
    serializer_class = TaskManagerUserSerializer
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        serializer = self.serializer_class(request.user)
        return Response(serializer.data)
