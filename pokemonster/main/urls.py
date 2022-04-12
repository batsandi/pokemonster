from django.urls import path

from pokemonster.main.views import ShowIndex, MyCustomonsView, AddCustomonView, CustomonWallView

urlpatterns = (
    path('', ShowIndex.as_view(), name='index'),
    path('customons/', MyCustomonsView.as_view(), name='my customons'),
    path('customons/add', AddCustomonView.as_view(), name='add customon'),
    path('wall/', CustomonWallView.as_view(), name='wall')
)
