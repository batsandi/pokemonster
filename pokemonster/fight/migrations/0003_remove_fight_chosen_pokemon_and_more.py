# Generated by Django 4.0.3 on 2022-04-14 19:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fight', '0002_pokemon_image_pokemon_types_fight'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='fight',
            name='chosen_pokemon',
        ),
        migrations.RemoveField(
            model_name='fight',
            name='enemy_pokemon',
        ),
    ]