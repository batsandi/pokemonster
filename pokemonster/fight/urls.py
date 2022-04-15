from django.urls import path

from pokemonster.fight.views import SelectPokemonView, FightView, CreateFightView, make_selection

urlpatterns = (
    path('select-pokemon', SelectPokemonView.as_view(), name='select pokemon'),
    path('fight', FightView.as_view(), name='fight'),
    path('create-fight/', CreateFightView.as_view(), name='create fight'),
    path('make-selection/<int:selection>', make_selection, name='make selection'),
)
