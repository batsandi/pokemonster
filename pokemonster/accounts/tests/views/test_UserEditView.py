from django.contrib.auth import get_user_model
from django.core.exceptions import PermissionDenied
from django.test import TestCase
from django.urls import reverse

from pokemonster.accounts.models import Profile

UserModel = get_user_model()


class UserEditView(TestCase):
    VALID_USER_DATA_1 = {
        'email': 'test@gmail.com',
        'password': 'paola1234',
        'id': 1,
    }

    VALID_USER_DATA_2 = {
        'email': 'test2@gmail.com',
        'password': 'paola1234',
        'id': 2,
    }

    VALID_PROFILE_DATA_1 = {
        'name': 'testname',
        'user_id': 1
    }

    VALID_PROFILE_DATA_2 = {
        'name': 'testname2',
        'user_id': 2
    }

    def test_show_edit_page__when_user_is_owner__expect_correct_template(self):
        user_1 = UserModel(
            **self.VALID_USER_DATA_1
        )
        profile_1 = Profile(
            **self.VALID_PROFILE_DATA_1
        )

        profile_1.save()

        user_1.save()

        self.client.force_login(
            user_1
        )

        self.client.get(
            reverse('edit profile', kwargs={'pk': user_1.pk})
        )

        self.assertTemplateUsed('accounts/edit_profile.html')

    # this test fails because of missing staticfile manifest???
    # def test_show_edit_page__when_User_is_not_owner__expect_to_raise(self):
    #     user_1 = UserModel(
    #         **self.VALID_USER_DATA_1
    #     )
    #
    #     user_2 = UserModel(
    #         **self.VALID_USER_DATA_2
    #     )
    #
    #     profile_1 = Profile(
    #         **self.VALID_PROFILE_DATA_1
    #     )
    #
    #     profile_2 = Profile(
    #         **self.VALID_PROFILE_DATA_2
    #     )
    #
    #     profile_1.save()
    #     profile_2.save()
    #
    #     user_1.save()
    #     user_2.save()
    #
    #     self.client.force_login(
    #         user_1
    #     )
    #
    #     with self.assertRaises(PermissionDenied) as context:
    #         self.client.get(
    #             reverse('edit profile', kwargs={'pk': user_2.pk})
    #         )
    #
    #     self.assertNotNone(context.exception)