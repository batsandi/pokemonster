
from django.test import TestCase
from django.urls import reverse


class LeaderboardViewTests(TestCase):
    def test_leaderboard__when_accessed__expect_correct_template(self):
        response = self.client.get(
            reverse('leaderboard')
        )

        self.assertTemplateUsed(response, 'accounts/leaderboard.html')
        
