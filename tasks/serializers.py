from rest_framework import serializers
from .models import Task
from profiles.models import TaskManagerUser
from tasks.models import TaskComment


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = TaskManagerUser
        fields = ["id", "username"]


class TaskCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = TaskComment
        fields = [
            "id",
            "comment",
            "owner",
            "owner_id",
            "task",
            "created_at",
            "updated_at",
        ]


class TaskSerializer(serializers.ModelSerializer):
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
        self.validated_data["owner_id"] = self.context["request"].user.id
        return super().save(**kwargs)
