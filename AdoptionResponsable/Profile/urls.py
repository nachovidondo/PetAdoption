from django.urls import path
from . import views
urlpatterns = [
    path('myprofile/', views.my_profile, name="myprofile")
]
