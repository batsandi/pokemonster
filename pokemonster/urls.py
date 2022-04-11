from django.contrib import admin
from django.urls import path, include
import pokemonster.accounts.signals

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('pokemonster.main.urls')),
    path('accounts/', include('pokemonster.accounts.urls'))
]
