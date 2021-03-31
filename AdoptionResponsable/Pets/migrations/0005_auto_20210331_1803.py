# Generated by Django 3.1.7 on 2021-03-31 18:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Pets', '0004_auto_20210331_1721'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pet',
            name='create_date',
            field=models.DateTimeField(auto_now=True, null=True, verbose_name='Fecha de Creacion'),
        ),
        migrations.AlterField(
            model_name='pet',
            name='date_found',
            field=models.DateField(blank=True, null=True, verbose_name='Fecha de encuentro'),
        ),
        migrations.AlterField(
            model_name='pet',
            name='description',
            field=models.TextField(blank=True, null=True, verbose_name='Descripcion'),
        ),
        migrations.AlterField(
            model_name='pet',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='', verbose_name='Imagenes'),
        ),
        migrations.AlterField(
            model_name='pet',
            name='looking_for_owner',
            field=models.BooleanField(blank=True, choices=[('Si', 'Si'), ('No', 'No')], null=True, verbose_name='Busca Dueño'),
        ),
        migrations.AlterField(
            model_name='pet',
            name='name',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Nombre'),
        ),
        migrations.AlterField(
            model_name='pet',
            name='phone_number',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Telefono de Contacto'),
        ),
        migrations.AlterField(
            model_name='pet',
            name='place_found',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Lugar encontrado'),
        ),
        migrations.AlterField(
            model_name='pet',
            name='race',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Raza'),
        ),
        migrations.AlterField(
            model_name='pet',
            name='treatments',
            field=models.TextField(blank=True, null=True, verbose_name='Tratamientos'),
        ),
        migrations.AlterField(
            model_name='pet',
            name='treatments_cost',
            field=models.FloatField(blank=True, null=True, verbose_name='Gastos de Tratamientos'),
        ),
        migrations.AlterField(
            model_name='pet',
            name='update_date',
            field=models.DateTimeField(auto_now_add=True, null=True, verbose_name='Fecha de Modificacion'),
        ),
    ]