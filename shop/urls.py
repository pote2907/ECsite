from django.urls import path
from . import views

app_name = 'shop'

urlpatterns = [
    path('', views.all_products, name='all_product'),
    path('<slug:c_slug>', views.all_products, name='products_by_category'),
    path('<slug:product_slug>/', views.product_detail, name='product_detail')
]