# Generated by Django 3.1.7 on 2021-04-02 05:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Index', '0002_indeximages'),
    ]

    operations = [
        migrations.AlterField(
            model_name='index',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='', verbose_name='Imagenes'),
        ),
        migrations.AlterField(
            model_name='index',
            name='subtitle',
            field=models.TextField(blank=True, null=True, verbose_name='Subtitulo'),
        ),
        migrations.AlterField(
            model_name='index',
            name='title',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Titulo'),
        ),
    ]
