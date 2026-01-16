#django uses these paths with its built in urlresolver to link to the correct view
#General Format: path('url', link to a view function, name of that view)

from django.urls import path
from . import views

# urls created to stem from the base url/ISP (in this case: http://127.0.0.1:8000/ or https://wrightaq.pythonanywhere.com/)
urlpatterns = [
    path('', views.post_list, name='post_list'), #making a list of all posts the root view when visited
    path('post/<int:pk>', views.post_detail, name='post_detail'), #to show the post details of a post specified by its pk (or primary key)
    path('post/new/', views.post_new, name='post_new'),
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
    path('drafts/', views.post_draft_list, name='post_draft_list'),#for unpublished posts
    path('post/<int:pk>/publish/', views.post_publish, name='post_publish'),
    path('post/<int:pk>/remove/', views.post_remove, name='post_remove'),
]