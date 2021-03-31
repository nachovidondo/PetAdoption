from django.db import models


class Pet(models.Model):
    owner_options= (('Si','Si'),('No','No'))
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200, verbose_name="Nombre", blank=True, null=True)
    race = models.CharField(max_length=200, verbose_name="Raza", blank=True, null=True)
    description = models.TextField(verbose_name="Descripcion", blank=True, null=True)
    date_found = models.DateField(verbose_name="Fecha de encuentro", blank=True, null=True)
    place_found = models.CharField(max_length=200, verbose_name="Lugar encontrado", blank=True, null=True)
    looking_for_owner = models.CharField(max_length=200, choices=owner_options, verbose_name="Busca Dueño", blank=True, null=True, default='Si')
    treatments = models.TextField(verbose_name="Tratamientos", blank=True, null=True)
    treatments_cost = models.FloatField(verbose_name="Gastos de Tratamientos", blank=True, null=True)
    phone_number = models.CharField(max_length=100, verbose_name="Telefono de Contacto", blank=True, null=True)
    image = models.ImageField(verbose_name="Imagenes", blank=True, null=True)
    create_date = models.DateTimeField(verbose_name="Fecha de Creacion",auto_now=True, blank=True, null=True)
    update_date = models.DateTimeField(verbose_name="Fecha de Modificacion",auto_now_add=True, blank=True, null=True)
    
    class Meta:
        verbose_name = "Mascota"
        verbose_name_plural = "Mascotas"
    
    def __str__(self):
        return self.name
    

    