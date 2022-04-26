from cloudinary import models as cloudinary_models
from django.contrib.auth import models as auth_models
from django.db import models

from pokemonster.accounts.managers import AppUserManager


class AppUser(auth_models.AbstractBaseUser, auth_models.PermissionsMixin):

    email = models.EmailField(
        unique=True
    )

    date_joined = models.DateTimeField(
        auto_now_add=True
    )

    is_staff = models.BooleanField(
        default=False
    )

    USERNAME_FIELD = 'email'

    objects = AppUserManager()


class Profile(models.Model):
    USERNAME_MAX_LENGTH = 35

    MYSTIC = 'Mystic'
    INSTINCT = 'Instinct'
    VALOR = 'Valor'
    UNAFFILIATED = 'Unaffiliated'

    FACTIONS = [(x, x) for x in (MYSTIC, INSTINCT, VALOR, UNAFFILIATED)]

    STARTING_CASH = 1000

    name = models.CharField(
        max_length=USERNAME_MAX_LENGTH,
        unique=True
        # validators=(
        #     MinLengthValidator(FIRST_NAME_MIN_LENGTH),
        #     validate_only_letters,
        #     # always_valid('asd'),
        # )
    )

    photo = cloudinary_models.CloudinaryField(
        'image',
        null=True,
        blank=True,
    )

    faction = models.CharField(
        max_length=max(len(x) for x, _ in FACTIONS),
        choices=FACTIONS,
        null=True,
        blank=True,
        default=UNAFFILIATED,
    )

    cash = models.IntegerField(
        default=STARTING_CASH
    )

    user = models.OneToOneField(
        AppUser,
        on_delete=models.CASCADE,
        primary_key=True
    )

    @property
    def get_wins_count(self):
        return len(self.fight_set.filter(owner_id=self.user_id, win=True))

    @property
    def get_losses_count(self):
        return len(self.fight_set.filter(owner_id=self.user_id, win=False))

    def __str__(self):
        return f'{self.name}'
