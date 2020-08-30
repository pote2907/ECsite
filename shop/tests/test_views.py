from django.test import TestCase


class ViewTest(TestCase):

    def test_fist_page(self):
        # localhost:8000/を取得
        response = self.client.get('/')
        # check status_code
        assert response.status_code == 200
