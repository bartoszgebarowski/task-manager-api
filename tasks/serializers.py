from rest_framework import serializers

from profiles.models import TaskManagerUser
from tasks.models import TaskComment

from .models import Task


class UserSerializer(serializers.ModelSerializer):
    """Serializer for user"""

    class Meta:
        model = TaskManagerUser
        fields = ["id", "username"]


class TaskCommentSerializer(serializers.ModelSerializer):
    """Serializer for task comments"""

    owner = UserSerializer(read_only=True)
    task_id = serializers.IntegerField(required=True)

    class Meta:
        model = TaskComment
        fields = [
            "id",
            "comment",
            "owner",
            "owner_id",
            "task_id",
            "created_at",
            "updated_at",
        ]
        read_only_fields = ["created_at", "updated_at", "task", "owner", "id"]

    def save(self, **kwargs):
        """Creates a task comment"""
        self.validated_data["owner_id"] = self.context["request"].user.id
        return super().save(**kwargs)


class TaskSerializer(serializers.ModelSerializer):
    """Serializer for tasks"""

    owner = UserSerializer(read_only=True)
    messages = TaskCommentSerializer(read_only=True, many=True)

    class Meta:
        model = Task
        fields = [
            "id",
            "owner",
            "owner_id",
            "title",
            "completed",
            "messages",
            "description",
            "created_at",
            "updated_at",
        ]

    def save(self, **kwargs):
        """Creates a task"""
        self.validated_data["owner_id"] = self.context["request"].user.id
        return super().save(**kwargs)
