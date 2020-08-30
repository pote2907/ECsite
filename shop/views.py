from django.shortcuts import render

from shop.models import Product


def all_products(request):
    # available=TrueのProductを取得
    products = Product.valid_objects.all()
    return render(request, 'shop/product_list.html', {'products': products})


def product_detail(request, product_slug):
    try:
        prodcut = Product.objects.get(slug=product_slug)
    except Exception as e:
        raise e
    return render(request, 'shop/product_detail.html', {'product': prodcut})