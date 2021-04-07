from django.shortcuts import render
from .models import Index, IndexImages
from django.views.generic import ListView, UpdateView
from django.urls import reverse_lazy
from . forms import FormEditIndex, FormEditIndexImages



class ListIndex(ListView):
    model = Index
    template_name = 'index.html'
    context_object_name = 'index'
    
#Administration
class AdminIndex(ListView):
    model = Index
    template_name = 'admin_index.html'

class IndexUpdate(UpdateView):
    model = Index
    template_name = 'edit_index.html'
    form_class = FormEditIndex
    success_url = reverse_lazy('admin_index')

class AdminIndexImages(ListView):
    model = IndexImages
    template_name = 'admin_index_images.html'
    
class IndexImagesUpdate(UpdateView):
    model = IndexImages
    template_name = 'edit_index_images.html'
    form_class = FormEditIndexImages
    success_url = reverse_lazy('admin_index')