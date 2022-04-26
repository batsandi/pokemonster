# Generated by Django 4.0.3 on 2022-04-26 04:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_alter_profile_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='gender',
        ),
        migrations.AddField(
            model_name='profile',
            name='faction',
            field=models.CharField(blank=True, choices=[('Mystic', 'Mystic'), ('Instinct', 'Instinct'), ('Valor', 'Valor')], default='Valor', max_length=8, null=True),
        ),
    ]
