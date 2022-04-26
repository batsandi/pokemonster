from django import forms
from django.core.exceptions import ValidationError

from pokemonster.common.mixins import FormWidgetsMixin
from pokemonster.fight.models import Fight


class CreateFightForm(FormWidgetsMixin, forms.ModelForm):
    def __init__(self, owner, selected_pokemon, win, fight_log,*args, **kwargs):
        super().__init__(*args, **kwargs)
        self._init_bootstrap_form_controls()
        self.owner = owner
        self.selected_pokemon = selected_pokemon
        self.win = win
        self.fight_log = fight_log

    def save(self, commit=True):
        fight = super().save(commit=False)

        fight.owner = self.owner
        fight.win = self.win
        fight.selected_pokemon = self.selected_pokemon
        fight.fight_log = self.fight_log

        if commit:
            fight.save()

        return fight

    class Meta:
        model = Fight
        fields = ('bet_amount',)
        widgets = {
            'bet_amount': forms.NumberInput(
                attrs={
                    'onkeyup': 'UpdateCash()',
                }
            ),
        }


    def clean_bet_amount(self):
        bet_amount = self.cleaned_data.get('bet_amount')
        cash = self.owner.cash
        if cash == 0:
            self.owner.cash = 1000
            self.owner.save()
            raise forms.ValidationError("Oh, you're broke. Here's another $1,000 to play with.")
        if bet_amount < 1:
            raise forms.ValidationError('Come on, bet some money...')
        if bet_amount > cash:
            raise forms.ValidationError('You cannot afford that amount.')
        return bet_amount

