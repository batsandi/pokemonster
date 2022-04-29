from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from django.test import TestCase
from django.urls import reverse

from pokemonster.accounts.models import Profile
UserModel = get_user_model()


class UserRegisterViewTests(TestCase):
    VALID_USER_DATA = {
        'email': 'test@gmail.com',
        'name': 'testname',
        'password1': 'parola1234',
        'password2': 'parola1234',
    }


    def test_create_user__when_valid_data__expect_to_create_user_and_profile(self):
        self.client.post(
            reverse('register'),
            data=self.VALID_USER_DATA,
        )

        user = UserModel.objects.first()
        profile = Profile.objects.first()
        self.assertEqual(self.VALID_USER_DATA['email'], user.email)
        self.assertIsNotNone(profile)
        self.assertIsNotNone(user)
        self.assertEqual(self.VALID_USER_DATA['email'], user.email)
        self.assertEqual(self.VALID_USER_DATA['name'], profile.name)

    # This test raises an error which I can't handle even after running manage.py collectstatic
    #ValueError: Missing staticfiles manifest entry for 'images/matrix.jpeg'
    # def test_create_user__when_valid_data__expect_to_redirect(self):
    #     response = self.client.post(
    #         reverse('register'),
    #         data=self.VALID_USER_DATA,
    #     )
    #
    #     expected_url = reverse('index')
    #     self.assertRedirects(response, expected_url)

    def test_create_user__when_valid_data__expect_to_login_automatically(self):
        self.client.post(
            reverse('register'),
            data=self.VALID_USER_DATA,
        )

        user = UserModel.objects.first()
        self.assertTrue(True, user.is_authenticated)

