from django.test import TestCase
from django.urls import reverse


# AttributeError: 'HttpResponseRedirect' object has no attribute 'context_data'
# class SelectPokemonView(TestCase):
#     def test_context__when_requested__expect_two_pokemons(self):
#         response = self.client.get(
#             reverse('select pokemon')
#         )
#
#         self.assertIsNotNone(response.context_data['pokemon_1'])
#         self.assertIsNotNone(response.context_data['pokemon_2'])

