from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from pokemonster.accounts.models import Profile
UserModel = get_user_model()


class UserLoginViewTests(TestCase):
    def test_login_user__when_valid_data__expect_to_login(self):
        pass

    def test_login_user__when_valid_data__expect_to_redirect(self):
        pass

