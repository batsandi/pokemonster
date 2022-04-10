from django.urls import path

from pokemonster.accounts.views import UserLoginView

urlpatterns = (
    path('login/', UserLoginView.as_view(), name='login'),
)
