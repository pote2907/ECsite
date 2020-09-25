from django.core.paginator import Paginator, EmptyPage, InvalidPage
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.conf import settings
from django.core.exceptions import ObjectDoesNotExist

from cart.models import CartItem, Cart, Order, OrderItem
from cart.views import _cart_id
from shop.models import Product, MediumCategory

import stripe


def all_products(request, c_slug=None, order=None, total=0):
    products_list = None
    category_page = None

    try:
        cart = Cart.objects.get(cart_id=_cart_id(request))
    except Cart.DoesNotExist:
        cart = Cart.objects.create(
            cart_id=_cart_id(request)
        )
        cart.save()

    cart_items = CartItem.objects.filter(cart=cart)

    if c_slug is not None:
        category_page = get_object_or_404(MediumCategory, slug=c_slug)
        # 特定のカテゴリーのみ取得
        products_list = Product.objects.filter(category=category_page, available=True)
    else:
        # available=TrueのProductを取得
        products_list = Product.valid_objects.all()

    if order == 'ascending':
        products_list = products_list.order_by('price')
    if order == 'descending':
        products_list = products_list.order_by('-price')
    # 3製品ごとに分割
    paginator = Paginator(products_list, 3)
    try:
        # 何ページ目なのか取得('page'が指定されなかったときは,1を取得)
        page = int(request.GET.get('page', '1'))
    except:
        page = 1
    try:
        # ページオブジェクト作成
        products = paginator.page(page)
    except (EmptyPage, InvalidPage):
        products = paginator.page(paginator.num_pages)

    for cart_item in cart_items:
        total += (cart_item.product.price * cart_item.quantity)

    # 以下決済処理
    stripe.api_key = settings.STRIPE_SECRET_KEY
    stripe_total = total
    description = 'New Order'
    data_key = settings.STRIPE_PUBLISHABLE_KEY
    if request.method == 'POST':
        # print(request.POST)
        try:
            token = request.POST['stripeToken']
            email = request.POST['stripeEmail']

            customer = stripe.Customer.create(
                email=email,
                source=token
            )
            charge = stripe.Charge.create(
                amount=stripe_total,
                currency='GBP',
                description=description,
                customer=customer.id
            )
            # オーダー作成
            try:
                order_details = Order.objects.create(
                    token=token,
                    total=total,
                    emailAddress=email,

                )
                order_details.save()
                for order_item in cart_items:
                    oi = OrderItem.objects.create(
                        product=order_item.product.name,
                        quantity=order_item.quantity,
                        price=order_item.product.price,
                        order=order_details
                    )
                    oi.save()

                    # 注文の時に在庫を減らす
                    products = Product.objects.get(id=order_item.product.id)
                    products.stock = int(order_item.product.stock - order_item.quantity)
                    products.save()
                    order_item.delete()

                    print('The order has been created')
                return redirect('shop:all_product')
            except ObjectDoesNotExist:
                pass

        except stripe.error.CardError as e:
            return False, e

    context = {
        'products': products,
        'category': category_page,
        'order': order,
        'cart_items': cart_items,
        'total': total,
        'data_key': data_key,
    }

    return render(request, 'shop/product_list.html', context)


def product_detail(request, product_slug, total=0):
    cart = Cart.objects.get(cart_id=_cart_id(request))
    cart_items = CartItem.objects.filter(cart=cart)
    try:
        product = Product.objects.get(slug=product_slug)
    except Exception as e:
        raise e

    for cart_item in cart_items:
        total += (cart_item.product.price * cart_item.quantity)

    context = {
        'product': product,
        'cart_items': cart_items,
        'total': total,
    }

    return render(request, 'shop/product_detail.html', context)


def size_ajax_response(request, product_slug):
    size = request.POST.getlist('name_input_text')[0]
    return HttpResponse(size)
