# Generated by Django 3.2 on 2021-05-03 18:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Profile', '0005_relationship'),
        ('Post', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='linked',
            field=models.ManyToManyField(blank=True, related_name='likes', to='Profile.Profile'),
        ),
    ]
