from django.urls import path
from . import views
from .views import EditAbout, CreateAbout, AboutList, AdminAbout

urlpatterns = [
    path('about_us',AboutList.as_view(), name="about_us"),
    path('create_about',CreateAbout.as_view(), name="create_about"),
    path('edit_about/<int:pk>/',EditAbout.as_view(), name="edit_about"),
    path('admin_about', AdminAbout.as_view(), name="admin_about"),
]