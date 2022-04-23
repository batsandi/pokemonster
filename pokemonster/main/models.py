from cloudinary import models as cloudinary_models
from django.db import models

from pokemonster.accounts.models import Profile


class Customon(models.Model):
    CUTE = 'Cute'
    ANNOYING = 'Annoying'
    FUNNY = 'Funny'
    ANGRY = 'Angry'
    SAD = 'Sad'
    AMAZING = 'Amazing'

    NAME_MAX_LENGTH = 35
    TYPES = [(x, x) for x in (CUTE, ANNOYING, FUNNY, ANGRY, SAD, AMAZING)]

    name = models.CharField(
        max_length=NAME_MAX_LENGTH
    )

    photo = cloudinary_models.CloudinaryField('image',)

    type = models.CharField(
        max_length=max(len(x) for (x, _) in TYPES),
        choices=TYPES,
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

    owner = models.ForeignKey(
        Profile,
        on_delete=models.CASCADE
    )
