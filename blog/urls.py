from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'), #making a list of all posts the root view when visited
]