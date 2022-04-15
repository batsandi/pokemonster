from django.db import models

from pokemonster.accounts.models import Profile


class Pokemon(models.Model):
    NAME_MAX_LENGTH = 30
    TYPE_MAX_LENGTH = 30

    name = models.CharField(
        max_length=NAME_MAX_LENGTH
    )

    image = models.URLField(
        null=True,
        blank=True
    )

    types = models.CharField(
        max_length=TYPE_MAX_LENGTH
    )

    hp = models.IntegerField()

    attack = models.IntegerField()

    defense = models.IntegerField()

    speed = models.IntegerField()

    def __str__(self):
        return self.name.title()


class Fight(models.Model):
    POKEMON_NAME_MAX_LENGTH = 35

    owner = models.ForeignKey(
        Profile,
        on_delete=models.CASCADE,
    )

    selected_pokemon = models.CharField(
        max_length=POKEMON_NAME_MAX_LENGTH
    )

    # chosen_pokemon = models.ManyToManyField(
    #     Pokemon,
    #     related_name='chosen'
    # )
    #
    # enemy_pokemon = models.ManyToManyField(
    #     Pokemon,
    #     related_name='enemy'
    # )

    win = models.BooleanField()

    bet_amount = models.IntegerField(
        #validate positive
    )

    fight_log = models.TextField()