from django.db.models import signals
from django.dispatch import receiver

from pokemonster.accounts.models import Profile
from pokemonster.fight.models import Fight


@receiver(signals.post_delete, sender=Profile)
def delete_user(sender, instance, **kwargs):
    instance.user.delete()


@receiver(signals.pre_save, sender=Fight)
def update_cash(sender, instance, **kwargs):
    if instance.win:
        instance.owner.cash += instance.bet_amount
    else:
        instance.owner.cash -= instance.bet_amount
    instance.owner.save()
