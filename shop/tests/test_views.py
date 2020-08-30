from django.test import TestCase
from django.urls import reverse

from shop.models import Category, Product

# product_listのURLパスを生成
PRODUCT_LIST_URL = reverse('shop:all_product')


class ViewTest(TestCase):

    def test_fist_page(self):
        # localhost:8000/を取得
        response = self.client.get('/')
        # check status_code
        assert response.status_code == 200

    def test_product_list_used_template(self):
        """localhost:8000/にアクセスした時に商品一覧が画面上に表示される"""
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'shop/product_list.html')

    def test_retrieve_products(self):
        category = Category.objects.create(
            name='Black Urban Cushion',
            slug='black-urban-cushion',
            description='description',
        )
        self.product1 = Product.objects.create(
            name='pag',
            slug='pag',
            description='cute pag',
            category=category,
            price=30,
            stock=10,
            available=True,
        )
        self.product2 = Product.objects.create(
            name='pig',
            slug='pig',
            description='cute pig',
            category=category,
            price=30,
            stock=10,
            available=True,
        )
        self.product3 = Product.objects.create(
            name='dog',
            slug='dog',
            description='cute pig',
            category=category,
            price=30,
            stock=10,
            available=False,
        )

        # product_listのViewを呼び出す
        response = self.client.get(PRODUCT_LIST_URL)

        # 作成したproductが含まれているか確認
        assert 'pag' in [product.name for product in response.context['products']]
        assert 'pig' in [product.name for product in response.context['products']]
        assert 'dog' not in [product.name for product in response.context['products']]
