from django.test import TestCase, Client
from django.urls import reverse

from shop.models import Category, Product

SEARCH_RESULT_URL = reverse('search:search_result')


class SearchTest(TestCase):

    def setUp(self):
        self.client = Client()
        self.category = Category.objects.create(
            name='Black Urban Cushion',
            slug='black-urban-cushion',
            description='description',
        )
        self.product1 = Product.objects.create(
            name='pag',
            slug='pag',
            description='cute pag',
            category=self.category,
            price=30,
            stock=10,
            available=True,
            image='test.png',
        )
        self.product2 = Product.objects.create(
            name='pig',
            slug='pig',
            description='cute pig',
            category=self.category,
            price=30,
            stock=10,
            available=True,
            image='test.png'
        )
        self.product3 = Product.objects.create(
            name='dog',
            slug='dog',
            description='cute pig',
            category=self.category,
            price=30,
            stock=10,
            available=False,
            image='test.png'
        )

    def test_access_to_search_result_view(self):
        response = self.client.get(SEARCH_RESULT_URL)
        assert response.status_code == 200

    def test_search_result(self):
        response = self.client.get(SEARCH_RESULT_URL, {'q': 'pag'})
        assert 'pag' in [product.name for product in response.context['products']]
        assert 'pig' not in [product.name for product in response.context['products']]
        assert 'dog' not in [product.name for product in response.context['products']]
