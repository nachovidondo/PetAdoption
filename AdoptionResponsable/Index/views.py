from django.shortcuts import render
from .models import Index
from django.views.generic import ListView


class ListIndex(ListView):
    model = Index
    template_name = 'index.html'
    context_object_name = 'index'