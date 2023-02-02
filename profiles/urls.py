from django.urls import path
from profiles import views

urlpatterns = [
    path('create-user/', views.CreateTaskManagerUserView.as_view(), name="create_user"),
]
