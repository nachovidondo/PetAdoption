from django.urls import path
from .views import ListIndex


urlpatterns = [
    path('',ListIndex.as_view(), name="index")
]