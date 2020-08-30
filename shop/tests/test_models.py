from django.test import TestCase

from shop.models import Category


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
