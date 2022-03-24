from django.db import models


class Category(models.Model):
    slug = models.SlugField(max_length=55, primary_key=True)
    name = models.CharField(max_length=55, unique=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name


class Color(models.Model):
    name = models.CharField(max_length=55, unique=True)
    image = models.ImageField(blank=True, null=True, upload_to='colors')


class Product(models.Model):
    CHOICES = (
        ('in stock', 'В наличии'),
        ('out of stock', 'Нет в наличии')
    )
    title = models.CharField(max_length=100)
    # image = models.ImageField(blank=True, null=True, upload_to='products')
    status = models.CharField(choices=CHOICES, max_length=20)
    description = models.TextField(blank=True)
    # price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField()  # хранения остатков данного продукта
    available = models.BooleanField(default=True)  # доступность товара
    created = models.DateTimeField(auto_now_add=True)  # хранит дату когда был создан объект.
    uploaded = models.DateTimeField(auto_now=True)  # время последнего обновления объекта
    article = models.CharField(max_length=55)
    # size = models.DecimalField(max_length=8, decimal_places=2)
    fabric = models.CharField(max_length=55, )
    material = models.CharField(max_length=55)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='category')
    color = models.ManyToManyField(Color)

    class Meta:
        ordering = ('name',)
        verbose_name = 'Product'
        verbose_name_plural = 'Products'
        index_together = ('id', 'slug')

    def __str__(self):
        return self.title


class Gallery(models.Model):
    image = models.ImageField(upload_to='gallery')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='images')


class ProductItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='product_item')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    size = models.DecimalField(max_length=8, decimal_places=2)
