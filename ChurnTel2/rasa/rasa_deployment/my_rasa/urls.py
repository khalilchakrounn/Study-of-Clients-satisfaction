from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('chatroom/', views.index, name='chatroom'),
]