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

    MALE = 'Male'
    FEMALE = 'Female'
    DO_NOT_SHOW = 'Do not show'

    GENDERS = [(x, x) for x in (MALE, FEMALE, DO_NOT_SHOW)]

    STARTING_CASH = 1000

    name = models.CharField(
        max_length=USERNAME_MAX_LENGTH,
        # validators=(
        #     MinLengthValidator(FIRST_NAME_MIN_LENGTH),
        #     validate_only_letters,
        #     # always_valid('asd'),
        # )
    )

    photo = models.ImageField(
        null=True,
        blank=True,
    )

    gender = models.CharField(
        max_length=max(len(x) for x, _ in GENDERS),
        choices=GENDERS,
        null=True,
        blank=True,
        default=DO_NOT_SHOW,
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
