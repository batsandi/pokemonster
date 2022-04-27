from django.contrib import admin
from django.contrib.auth import get_user_model

from pokemonster.accounts.models import Profile, AppUser

UserModel = get_user_model()


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(UserModel)
class UserAdmin(admin.ModelAdmin):
    list_display = ('email',)
