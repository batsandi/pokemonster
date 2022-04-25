from django.contrib.auth import get_user_model
from django.contrib.auth import forms as auth_forms
from django import forms

from pokemonster.accounts.models import Profile
from pokemonster.common.mixins import FormWidgetsMixin

UserModel = get_user_model()


class UserRegisterForm(FormWidgetsMixin, auth_forms.UserCreationForm):
    name = forms.CharField(
        max_length=Profile.USERNAME_MAX_LENGTH,
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._init_bootstrap_form_controls()
        self.fields['password1'].help_text=None
        self.fields['password2'].help_text=None

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
        model = UserModel
        fields = ['email', 'name', 'password1', 'password2']
        # The below does nothing, Since all fields are declared explicitly.
        # widgets = {
        #     'name': forms.EmailInput(
        #         attrs={
        #             'placeholder': 'Enter email'
        #         },
        #     ),
        # }


class UserLoginForm(FormWidgetsMixin, auth_forms.AuthenticationForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._init_bootstrap_form_controls()