from django.contrib import admin

from pokemonster.accounts.models import Profile, AppUser


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(AppUser)
class UserAdmin(admin.ModelAdmin):
    list_display = ('email',)
