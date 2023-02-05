from rest_framework import serializers
from .models import Task
from profiles.models import TaskManagerUser

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = TaskManagerUser
        fields = [
            'id', 'username'
        ]

class TaskSerializer(serializers.ModelSerializer):
    assignees = UserSerializer(many=True)
    owner = UserSerializer()
    class Meta:
        model = Task
        fields = [
            'id', 'owner', 'assignees', 'description', 'created_at', 'updated_at'
        ]
