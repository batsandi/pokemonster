from django.urls import path

from pokemonster.main.views import ShowIndex

urlpatterns = (
    path('', ShowIndex.as_view(), name='index'),
)
