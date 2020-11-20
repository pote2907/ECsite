from django.contrib import admin

from .models import LargeCategory, MediumCategory, Product


class LargeCategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(LargeCategory, LargeCategoryAdmin)


class MediumCategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(MediumCategory, MediumCategoryAdmin)


class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'stock_m', 'stock_l', 'stock_xl', 'available', 'created', 'updated']
    list_editable = ['price', 'available']
    prepopulated_fields = {'slug': ('name',)}
    list_per_page = 20


admin.site.register(Product, ProductAdmin)
