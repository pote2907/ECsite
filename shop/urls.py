from django.urls import path
from . import views

app_name = 'shop'

urlpatterns = [
    path('', views.all_products, name='all_product'),
    path('<slug:product_slug>/', views.product_detail, name='product_detail')
]