from django import forms
from django.core.exceptions import ValidationError

from pokemonster.fight.models import Fight


class CreateFightForm(forms.ModelForm):
    def __init__(self, owner, selected_pokemon, win,*args, **kwargs):
        super().__init__(*args, **kwargs)
        self.owner = owner
        self.selected_pokemon = selected_pokemon
        self.win = win

    def save(self, commit=True):
        fight = super().save(commit=False)

        fight.owner = self.owner
        fight.win = self.win
        fight.selected_pokemon = self.selected_pokemon

        if commit:
            fight.save()

        return fight

    class Meta:
        model = Fight
        fields = ('bet_amount',)

    def clean_bet_amount(self):
        bet_amount = self.cleaned_data.get('bet_amount')
        cash = self.owner.cash
        if bet_amount < 1:
            raise forms.ValidationError('Come on, bet some money...')
        if bet_amount > cash:
            raise forms.ValidationError('You cannot afford that amount.')
        return bet_amount

