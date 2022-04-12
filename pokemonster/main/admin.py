from django.contrib import admin

from pokemonster.main.models import Customon


@admin.register(Customon)
class CustomonAdmin(admin.ModelAdmin):
    list_display = ('name', 'owner')