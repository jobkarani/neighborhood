# Generated by Django 3.2.9 on 2022-01-10 03:52

import cloudinary.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20220110_0642'),
    ]

    operations = [
        migrations.RenameField(
            model_name='neighbourhood',
            old_name='admin',
            new_name='user',
        ),
        migrations.AddField(
            model_name='neighbourhood',
            name='about',
            field=models.TextField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='neighbourhood',
            name='cop_dail',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='neighbourhood',
            name='health_dail',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='neighbourhood',
            name='photo',
            field=cloudinary.models.CloudinaryField(max_length=255, null=True, verbose_name='image'),
        ),
    ]
