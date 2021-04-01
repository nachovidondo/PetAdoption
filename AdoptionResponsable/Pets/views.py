from django.shortcuts import render
from .models import Pet
from django.views.generic import ListView, CreateView, DetailView, DeleteView, UpdateView, View
from .forms import FormsPet
from django.urls.base import reverse_lazy



class Index(ListView):
    model = Pet
    template_name = 'index.html'


class ListofPets(ListView):
    model = Pet
    template_name = 'list_pet.html'
    context_object_name = 'pets'
    

class CreatePet(CreateView):
    model = Pet
    template_name = 'create_pet.html'
    form_class = FormsPet
    success_url = reverse_lazy('list_pet')
    

class DetailPet(DetailView):
    model = Pet
    template_name = 'detail_pet.html'
    context_object_name = 'pets'
    
    
class DeletePet(DeleteView):
    model = Pet
    success_url = reverse_lazy('list_pet')

class UpdatePet(UpdateView):
    model = Pet
    template_name = 'update_pet.html'
    context_object_name = 'pets'
    form_class = FormsPet
    success_url = reverse_lazy ('list_pet')