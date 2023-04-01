from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        """
        Returns a boolean to whether user has read access by default.
        Write permissions are only allowed to object owner.
        """
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.owner == request.user
