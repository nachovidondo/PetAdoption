# Generated by Django 3.2 on 2021-05-03 00:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Profile', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='avatar',
            field=models.ImageField(default='Imagenes/avatar1.png', upload_to='avatars/'),
        ),
    ]
