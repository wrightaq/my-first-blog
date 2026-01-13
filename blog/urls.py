from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'), #making a list of all posts the root view when visited
    path('post/<int:pk>', views.post_detail, name='post_detail'), #to show the post details of a post specified by its pk (or primary key)
]