from django.db import models
from django.urls import reverse


class ValidManager(models.Manager):
    """available=TrueのProductだけ返すようにする"""

    def get_queryset(self):
        return super(ValidManager, self).get_queryset().filter(available=True)


class LargeCategory(models.Model):
    """大カテゴリー"""
    name = models.CharField(max_length=250, unique=True)
    slug = models.SlugField(max_length=250, unique=True)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='category', blank=True)

    def get_url(self):
        return reverse('shop:products_by_large_category', args=[self.slug])

    def __str__(self):
        return self.name


class MediumCategory(models.Model):
    """中カテゴリー"""
    large_category = models.ForeignKey(LargeCategory, on_delete=models.CASCADE)
    name = models.CharField(max_length=250, unique=True)
    slug = models.SlugField(max_length=250, unique=True)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='category', blank=True)

    def get_url(self):
        return reverse('shop:products_by_medium_category', args=[self.slug])

    def ascending(self):
        return reverse('shop:sorted_category_products', args=['ascending', self.slug])

    def descending(self):
        return reverse('shop:sorted_category_products', args=['descending', self.slug])

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=250, unique=True)
    slug = models.SlugField(max_length=250, unique=True)
    description = models.TextField(blank=True)
    category = models.ForeignKey(MediumCategory, on_delete=models.CASCADE)
    price = models.IntegerField()
    # stock = models.IntegerField()
    stock_m = models.IntegerField(default=0)
    stock_l = models.IntegerField(default=0)
    stock_xl = models.IntegerField(default=0)
    size = models.BooleanField(default=True)
    available = models.BooleanField(default=True)
    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)
    main_image = models.ImageField(upload_to='product')
    sub_image1 = models.ImageField(upload_to='product')
    sub_image2 = models.ImageField(upload_to='product')
    sub_image3 = models.ImageField(upload_to='product')


    # デフォルトのマネージャー
    objects = models.Manager()
    # カスタムマネージャー
    valid_objects = ValidManager()

    def get_url(self):
        return reverse('shop:product_detail', args=[self.slug])

    class Meta:
        ordering = ('name',)
        verbose_name = 'product'
        verbose_name_plural = 'products'

    def __str__(self):
        return self.name
