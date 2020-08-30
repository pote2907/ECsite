from django.test import TestCase
from django.urls import reverse

SEARCH_RESULT_URL = reverse('search:search_result')


class SearchTest(TestCase):

    def test_access_to_search_result_view(self):
        response = self.client.get(SEARCH_RESULT_URL)
        assert response.status_code == 200
