from django.test import TestCase

from shop.models import Category, Product


class ModelTest(TestCase):

    def test_create_category(self):
        name = 'Black Urban Cushion'
        slug = 'black-urban-cushion'
        description = 'description'

        # create Category object
        Category.objects.create(
            name=name,
            slug=slug,
            description=description
        )
        category = Category.objects.all()[0]

        assert str(category) == category.name

    def test_create_product(self):
        category = Category.objects.create(
            name='Black Urban Cushion',
            slug='black-urban-cushion',
            description='description',
        )
        Product.objects.create(
            name='pag dog',
            slug='pag-dog',
            description='cute pag',
            category=category,
            price=30,
            stock=10,
            available=True,
        )
        product = Product.objects.all()[0]

        assert str(product) == product.name
