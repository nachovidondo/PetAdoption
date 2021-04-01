from django.shortcuts import render
from django.views.generic import CreateView, UpdateView,  ListView
from .models import About
from  .forms import FormAbout
from django.urls import reverse_lazy


class AboutList(ListView):
    model = About
    template_name = 'about.html'
    

class CreateAbout(CreateView):
    model = About
    template_name = "create_about.html"
    form_class = FormAbout
    success_url = reverse_lazy('list_pet')
    

class EditAbout(UpdateView):
    model = About
    template_name = "edit_about.html"
    form_class = FormAbout
    success_url = reverse_lazy('list_pet')