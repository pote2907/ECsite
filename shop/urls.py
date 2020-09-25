from django.urls import path
from . import views

app_name = 'shop'

urlpatterns = [
    path('', views.all_products, name='all_product'),
    # path('from_cart', views.all_products_cart_on, name='all_product_cart_on'),
    path('<slug:c_slug>', views.all_products, name='products_by_medium_category'),
    path('order/<str:order>', views.all_products, name='sorted_products'),
    path('order/<str:order>/<slug:c_slug>', views.all_products, name='sorted_category_products'),
    path('<slug:product_slug>/', views.product_detail, name='product_detail'),
    path('<slug:product_slug>/size/', views.size_ajax_response, name='size_ajax'),
    path('thank_you/order', views.thanks, name='thanks')
]
