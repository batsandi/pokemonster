# Generated by Django 4.0.3 on 2022-04-23 18:55

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_profile_cash'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='photo',
            field=cloudinary.models.CloudinaryField(blank=True, max_length=255, null=True, verbose_name='image'),
        ),
    ]