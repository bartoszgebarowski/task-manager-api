from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from profiles import views

urlpatterns = [
    path(
        "create-user/",
        views.CreateTaskManagerUserView.as_view(),
        name="create_user",
    ),
    path("token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("user/", views.UserDetailView.as_view(), name="user_detail_view"),
]
