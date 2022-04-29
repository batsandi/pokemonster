import random
import requests
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.views import generic as views

from pokemonster.fight.forms import CreateFightForm
from pokemonster.fight.helpers import Battle, convert_pokemon_data
from pokemonster.fight.models import Pokemon, Fight


class SelectPokemonView(LoginRequiredMixin, views.TemplateView):
    MIN_POKE_ID = 1
    MAX_POKE_ID = 151
    API_BASE_URL = 'https://pokeapi.co/api/v2/pokemon/'
    template_name = 'fight/select_pokemon.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        id_1 = random.randint(self.MIN_POKE_ID, self.MAX_POKE_ID)
        id_2 = random.randint(self.MIN_POKE_ID, self.MAX_POKE_ID)

        pokemon_1_data = convert_pokemon_data(
            requests.get(f'{self.API_BASE_URL}{id_1}')\
            .json()
        )
        pokemon_2_data = convert_pokemon_data(
            requests.get(f'{self.API_BASE_URL}{id_2}')\
            .json()
        )

        self.request.session['id_1'] = id_1
        self.request.session['id_2'] = id_2

        pokemon_1 = Pokemon(**pokemon_1_data)
        pokemon_2 = Pokemon(**pokemon_2_data)

        pokemon_1.save()
        pokemon_2.save()

        context.update({
            'pokemon_1': pokemon_1,
            'pokemon_2': pokemon_2,
        })

        return context


@login_required
def make_selection(request, selection):
    if selection == 1:
        request.session['selected_pokemon'] = request.session.get('id_1')
        request.session['enemy_pokemon'] = request.session.get('id_2')
    elif selection == 2:
        request.session['selected_pokemon'] = request.session.get('id_2')
        request.session['enemy_pokemon'] = request.session.get('id_1')

    return redirect('make bet')


class MakeBetView(LoginRequiredMixin, views.CreateView):
    form_class = CreateFightForm
    template_name = 'fight/make_bet.html'
    # success_url = reverse_lazy('fight result')

    def get_success_url(self):
        return reverse('fight result', kwargs={'pk': self.object.pk})

    def get_form_kwargs(self):
        selected_pokemon_id = self.request.session.get('selected_pokemon')
        enemy_pokemon_id = self.request.session.get('enemy_pokemon')

        # selected_pokemon_data = self.request.session.get('selected_pokemon')
        # enemy_pokemon_data = self.request.session.get('enemy_pokemon')

        selected_pokemon = Pokemon.objects.get(poke_index=selected_pokemon_id)
        enemy_pokemon = Pokemon.objects.get(poke_index=enemy_pokemon_id)

        # selected_pokemon = Pokemon(**selected_pokemon_data)
        # enemy_pokemon = Pokemon(**enemy_pokemon_data)

        kwargs = super().get_form_kwargs()
        kwargs['owner'] = self.request.user.profile
        kwargs['selected_pokemon'] = selected_pokemon

        winner, fight_log = Battle.fight(selected_pokemon, enemy_pokemon)
        kwargs['win'] = winner == kwargs['selected_pokemon']
        kwargs['fight_log'] = fight_log

        return kwargs


class FightResultView(LoginRequiredMixin, views.DetailView):
    template_name = 'fight/fight_result.html'
    model = Fight

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        fight_log = self.object.fight_log.split(', ')
        context.update({
            'split_fight_log': fight_log,
        })

        return context

