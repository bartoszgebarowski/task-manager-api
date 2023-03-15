from rest_framework import serializers
from .models import Task
from profiles.models import TaskManagerUser


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = TaskManagerUser
        fields = ["id", "username"]


class TaskSerializer(serializers.ModelSerializer):
    assignees_details = UserSerializer(read_only=True, many=True)
    owner = UserSerializer(read_only=True)

    class Meta:
        model = Task
        fields = [
            "id",
            "owner",
            "owner_id",
            "title",
            "assignees",
            "assignees_details",
            "description",
            "created_at",
            "updated_at",
        ]

    def save(self, **kwargs):
        self.validated_data["owner_id"] = self.context["request"].user.id
        return super().save(**kwargs)
