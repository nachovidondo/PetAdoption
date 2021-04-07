from django import forms
from .models import Index, IndexImages



class FormEditIndex(forms.ModelForm):
    class Meta:
        model = Index
        fields = ['title','subtitle']

class  FormEditIndexImages(forms.ModelForm):
    class Meta:
        model = IndexImages
        fields = '__all__'