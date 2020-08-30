from django.test import TestCase
from django.utils import timezone

from cart.models import Cart, CartItem
from shop.models import Category, Product


class ModelTest(TestCase):

    def test_create_cart(self):
        Cart.objects.create(
            cart_id='USERONLY',
            date_added=timezone.now()
        )
        cart = Cart.objects.all()[0]
        assert str(cart) == cart.cart_id

    def test_create_cartitem(self):
        category = Category.objects.create(
            name='Black Urban Cushion',
            slug='black-urban-cushion',
            description='description',
        )

        product = Product.objects.create(
            name='pag',
            slug='pag',
            description='cute pag',
            category=category,
            price=30,
            stock=10,
            available=True,
            image='test.png',
        )

        cart = Cart.objects.create(
            cart_id='USERONLY',
            date_added=timezone.now()
        )

        CartItem.objects.create(
            product=product,
            cart=cart,
            quantity=3,
            active=True
        )

        cart_item = CartItem.objects.all()[0]
        assert str(cart_item) == cart_item.product.name
