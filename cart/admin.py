from django.contrib import admin

from .models import CartItem, Cart, OrderItem, Order

class CartAdmin(admin.ModelAdmin):
    actions = ['delete_unused_cart', ]

    def delete_unused_cart(self, request, queryset):
        """カートアイテムが入っていないカートを削除する"""
        for cart in queryset:
            cart_items = CartItem.objects.filter(cart=cart)
            if cart_items.count() == 0:
                cart.delete()

    delete_unused_cart.short_description = 'カートアイテムが入っていないカートを削除'


admin.site.register(Cart, CartAdmin)
admin.site.register(CartItem)
admin.site.register(Order)
admin.site.register(OrderItem)

