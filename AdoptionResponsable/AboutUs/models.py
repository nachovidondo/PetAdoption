from django.db import models


class About(models.Model):
    title = models.CharField(max_length=200, verbose_name="Titulo")
    description = models.TextField(verbose_name="Descripcion")
    class Meta:
        verbose_name = "Acerca Nuestro"
        
    def __str__(self):
        return self.title