from django.db.models import signals
from django.dispatch import receiver

from pokemonster.accounts.models import Profile


@receiver(signals.post_delete, sender=Profile)
def delete_user(sender, instance, **kwargs):
    instance.user.delete()
