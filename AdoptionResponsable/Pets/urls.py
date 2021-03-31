from django.urls import path
from .views import ListofPets, CreatePet, DetailPet, DeletePet, UpdatePet



urlpatterns = [
    path('list_pet',ListofPets.as_view(), name='list_pet'),
    path('create_pet',CreatePet.as_view(), name='create_pet'),
    path('detail_pet/<int:pk>/',DetailPet.as_view(), name='detail_pet'),
    path('delete_pet/<int:pk>/',DeletePet.as_view(), name="delete_pet"),
    path('update_pet/<int:pk>/',UpdatePet.as_view(), name='update_pet')
]
