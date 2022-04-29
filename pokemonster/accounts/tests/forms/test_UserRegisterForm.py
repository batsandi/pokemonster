from django.test import TestCase
from django.urls import reverse


class UserRegisterFormTests(TestCase):
    def test_form__when_initialized__expect_widget_attrs(self):
        self.client.get(
            reverse('register')
        )
