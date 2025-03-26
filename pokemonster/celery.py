import os

from pokemonster.celery import Celery

# Uncomment below if the other line doesn't work
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'pokemonster.settings')
# DJANGO_SETTINGS_MODULE = os.getenv('DJANGO_SETTINGS_MODULE', 'pokemonster.settings')

app = Celery('pokemonster')

app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()


@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')