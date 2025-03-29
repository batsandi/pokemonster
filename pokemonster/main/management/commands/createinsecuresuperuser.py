from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    def handle(self, *args, **options):
        User = get_user_model()  # Ensures you get your custom user model

        email = 'super@user.com'
        if not User.objects.filter(email=email).exists():
            User.objects.create_superuser(
                email=email,
                password='P4ssw0rd',
            )