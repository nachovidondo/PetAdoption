from django.urls import path
from django.contrib.auth.decorators import login_required
from .views import ListIndex, AdminIndex, IndexUpdate, AdminIndexImages, IndexImagesUpdate


urlpatterns = [
    path('',login_required(ListIndex.as_view()), name="index"),
    path('admin_index',AdminIndex.as_view(), name="admin_index"),
    path('edit_index/<int:pk>/',IndexUpdate.as_view(), name="edit_index"),
    path('admin_index_images',AdminIndexImages.as_view(), name="admin_index_images"),
    path('edit_index_images/<int:pk>/',IndexImagesUpdate.as_view(), name="edit_index_images"),
]