from django.urls import path
from .views import  ListUser, DetailUser


urlpatterns = [
    path('users', ListUser.as_view(), name='users'),
    path('users/<int:pk>/', DetailUser.as_view(), name='singleuser'),
]