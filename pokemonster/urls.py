from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from pokemonster.common import signals

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('pokemonster.main.urls')),
    path('accounts/', include('pokemonster.accounts.urls')),
    path('fight/', include('pokemonster.fight.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
