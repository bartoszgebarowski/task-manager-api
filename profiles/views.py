from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from profiles.serializers import TaskManagerUserSerializer


class CreateTaskManagerUserView(generics.CreateAPIView):
    """Creates new user in application"""

    serializer_class = TaskManagerUserSerializer


class UserDetailView(generics.RetrieveAPIView):
    """Generic class for retrieving authenticated user"""

    serializer_class = TaskManagerUserSerializer
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        """Retrieve authenticated user"""
        serializer = self.serializer_class(request.user)
        return Response(serializer.data)
