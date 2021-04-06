from django.contrib import admin
from .models import Pet, PetImages


class PetImagesAdmin(admin.StackedInline):
    model = PetImages
    
    
@admin.register(Pet)


class PetAdmin(admin.ModelAdmin):
    inlines=[PetImagesAdmin]


