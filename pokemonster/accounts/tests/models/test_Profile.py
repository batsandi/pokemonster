from django.contrib.auth import get_user_model
from django.core.files.uploadedfile import SimpleUploadedFile
from django.test import TestCase

from pokemonster.accounts.models import Profile
from pokemonster.settings import BASE_DIR

UserModel = get_user_model()


class ProfileTests(TestCase):
    FAKE_FILE = SimpleUploadedFile(
        name='test_image.jpg',
        content=open(
            BASE_DIR / 'static' / 'images' / 'not_found.jpg',
            'rb'
        ).read(),
        content_type='image/jpeg'
    )

    VALID_PROFILE_DATA = {
        'name': 'testname',
        'photo': FAKE_FILE,
        'user_id': 1
    }

    VALID_USER_DATA = {
        'email': 'test@gmail.com',
        'password': 'parola1234',
        'id': 1
    }

    def test_create_profile__when_valid_data__expect_to_create(self):
        user = UserModel(
            **self.VALID_USER_DATA
        )
        user.save()

        profile = Profile(
            **self.VALID_PROFILE_DATA
        )
        profile.save()

        self.assertIsNotNone(Profile.objects.first())
        self.assertIsNotNone(profile.photo)
        self.assertEqual(self.VALID_PROFILE_DATA['name'], profile.name)

    def test_create_user__when_user_with_ame_name_exists__expect_to_raiese(self):
        pass

    def test_get_win_count__when_some_wins__expect_correct_wins(self):
        pass

    def test_get_loss_count__when_some_wins__expect_correct_losses(self):
        pass