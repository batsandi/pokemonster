# Generated by Django 4.0.3 on 2022-04-15 11:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_customon_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customon',
            name='photo',
            field=models.ImageField(default='default', upload_to=''),
            preserve_default=False,
        ),
    ]