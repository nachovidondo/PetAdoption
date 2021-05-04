from django.urls import path
from . import views


urlpatterns = [
    path('main/', views.post_comments_create_and_list_view, name="main")
]