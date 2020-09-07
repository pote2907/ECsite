from django.core.paginator import Paginator, EmptyPage, InvalidPage
from django.shortcuts import render, get_object_or_404

from shop.models import Product, Category


def all_products(request, c_slug=None):
    products_list = None
    category_page = None

    if c_slug is not None:
        category_page = get_object_or_404(Category, slug=c_slug)
        # 特定のカテゴリーのみ取得
        products_list = Product.objects.filter(category=category_page, available=True)
    else:
        # available=TrueのProductを取得
        products_list = Product.valid_objects.all()
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

    return render(request, 'shop/product_list.html', {'products': products, 'category': category_page})


def product_detail(request, product_slug):
    try:
        product = Product.objects.get(slug=product_slug)
    except Exception as e:
        raise e
    return render(request, 'shop/product_detail.html', {'product': product})
