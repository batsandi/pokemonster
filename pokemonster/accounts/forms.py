from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django import forms

from pokemonster.accounts.models import Profile


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    name = forms.CharField(
        max_length=Profile.USERNAME_MAX_LENGTH
    )

    def save(self, commit=True):
        user = super().save(commit=commit)
        profile = Profile(
            name=self.cleaned_data['name'],
            user=user,
        )

        if commit:
            profile.save()
        return user

    class Meta:
        model = get_user_model()
        fields = ('email', 'password1', 'password2', 'name')

