from django.contrib import admin
from .models import Index, IndexImages


class IndexImagesAdmin(admin.StackedInline):
    model = IndexImages
    
@admin.register(Index)

class IndexAdmin(admin.ModelAdmin):
    inlines=[IndexImagesAdmin]
    class Meta:
        model = Index

