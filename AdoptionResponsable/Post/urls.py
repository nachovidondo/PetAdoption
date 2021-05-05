from django.urls import path
from .views import PostDeleteView, PostUpdateView
from . import views


urlpatterns = [
    path('main/', views.post_comments_create_and_list_view, name="main"),
    path('liked', views.like_unlike_post, name="liked"),
    path('delete/<int:pk>/', PostDeleteView.as_view(), name="post-delete"),
    path('update/<int:pk>/', PostUpdateView.as_view(), name="post-update")
]