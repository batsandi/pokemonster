from django.urls import path

from pokemonster.fight.views import SelectPokemonView, MakeBetView, make_selection, FightResultView
urlpatterns = (
    path('select-pokemon', SelectPokemonView.as_view(), name='select pokemon'),
    path('make-selection/<int:selection>', make_selection, name='make selection'),
    path('make-bet/', MakeBetView.as_view(), name='make bet'),
    path('result/<int:pk>', FightResultView.as_view(), name='fight result'),
)

