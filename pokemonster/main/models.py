from django.db import models

from pokemonster.accounts.models import Profile


class Customon(models.Model):
    CUTE = 'Cure'
    ANNOYING = 'Annoying'
    FUNNY = 'Funny'

    NAME_MAX_LENGTH = 35
    TYPES = [(x, x) for x in (CUTE, ANNOYING, FUNNY)]

    name = models.CharField(
        max_length=NAME_MAX_LENGTH
    )

    photo = models.ImageField(
        null=True,
        blank=True
    )

    type = models.CharField(
        max_length=max(len(x) for (x, _) in TYPES),
        choices=TYPES,
    )

    likes = models.IntegerField(
        default=0
    )

    owner = models.ForeignKey(
        Profile,
        on_delete=models.CASCADE
    )


class Comment(models.Model):
    text = models.TextField()

    customon = models.ForeignKey(
        Customon,
        on_delete=models.CASCADE
    )

    time = models.DateTimeField(
        auto_now_add=True
    )
