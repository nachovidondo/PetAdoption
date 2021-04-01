from django.urls import path
from .views import Index, ListofPets, CreatePet, DetailPet, DeletePet, UpdatePet
from django.contrib.auth.decorators import login_required



urlpatterns = [
    path('', Index.as_view(), name="index"),
    path('list_pet',login_required(ListofPets.as_view()), name='list_pet'),
    path('create_pet',login_required(CreatePet.as_view()), name='create_pet'),
    path('detail_pet/<int:pk>/',login_required(DetailPet.as_view()), name='detail_pet'),
    path('delete_pet/<int:pk>/',login_required(DeletePet.as_view()), name="delete_pet"),
    path('update_pet/<int:pk>/',login_required(UpdatePet.as_view()), name='update_pet'),
]
