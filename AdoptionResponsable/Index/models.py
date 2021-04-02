from django.db import models


class Index(models.Model):
    title = models.CharField(max_length=200, verbose_name="Titulo", blank=True, null=True)
    subtitle = models.TextField(verbose_name="Subtitulo", blank=True, null=True)
    image = models.ImageField(verbose_name="Imagenes", blank=True, null=True)
    class Meta:
        verbose_name = "Index"
    def __str__(self):
        return self.title


class IndexImages(models.Model):
    index = models.ForeignKey(Index, default =None ,on_delete=models.CASCADE)
    image = models.ImageField(upload_to ="Imagenes",verbose_name="Imagenes") 
    class Meta:
        verbose_name="Agregar una Imagen"
        verbose_name_plural="Agregar mas Imagenes"
        def __str__(self):
            return self.index
    