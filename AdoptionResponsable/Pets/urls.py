from django.urls import path
from .views import  (
    ListofPets, CreatePet, DetailPet, DeletePet, UpdatePet, AdminList
    )
from django.contrib.auth.decorators import login_required



urlpatterns = [
    path('list_pet',login_required(ListofPets.as_view()), name='list_pet'),
    path('create_pet',login_required(CreatePet.as_view()), name='create_pet'),
    path('detail_pet/<int:pk>/',login_required(DetailPet.as_view()), name='detail_pet'),
    path('delete_pet/<int:pk>/',login_required(DeletePet.as_view()), name="delete_pet"),
    path('update_pet/<int:pk>/',login_required(UpdatePet.as_view()), name='update_pet'),
    path('admin_pet', AdminList.as_view(), name="admin_pet"),
]
