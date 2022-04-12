from django import forms

from pokemonster.main.models import Customon


class AddCustomonForm(forms.ModelForm):
    def __init__(self, owner, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.owner = owner

    def save(self, commit=True):
        customon = super().save(commit=False)
        customon.owner = self.owner
        if commit:
            customon.save()
        return customon

    class Meta:
        model = Customon
        fields = ('name', 'type', 'photo')
