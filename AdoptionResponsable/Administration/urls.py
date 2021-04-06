from django.urls import path
from . import views

urlpatterns = [
    path('administration/',views.administration, name="administration"),
]