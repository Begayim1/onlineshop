from django.core.exceptions import ValidationError
from django.db import models
from colorful.fields import RGBColorField

            # """Товары"""

class Category(models.Model):
    name = models.CharField(max_length=55, unique=True)
    image = models.ImageField()

    class Meta:
        ordering = ('name',)
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name


class Color(models.Model):
    name = models.CharField(max_length=20)
    color = RGBColorField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Color'
        verbose_name_plural = 'Colors'

# class Size(models.Model):
#     size = models.CharField(max_length=20)
#
#     class Meta:
#         ordering = ('size',)
#
#     def __str__(self):
#         return self.size


class Product(models.Model):

    title = models.CharField(max_length=100) #название
    description = models.TextField(blank=True, max_length=400) #описание
    # created = models.DateTimeField(default=True)  # хранит дату когда был создан объект.
    article = models.CharField(max_length=55) #артикл
    fabric = models.CharField(max_length=55, ) #cостав ткани
    material = models.CharField(max_length=55) #материал
    quantity_in_line = models.PositiveSmallIntegerField(default=0) #количество в линейке
    price = models.DecimalField(max_digits=5, decimal_places=2)
    old_price = models.PositiveIntegerField(null=True, blank=True) #старая цена
    size = models.CharField(max_length=55)
    color = models.ManyToManyField(Color, verbose_name=Color, related_name='product')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True)
    hit_of_sales = models.BooleanField(default=False) #хит продаж
    new = models.BooleanField(default=True) #новинки


    # uploaded = models.DateTimeField(auto_now=True)  # время последнего обновления объекта
    # stock = models.PositiveIntegerField()  # хранения остатков данного продукта
    # available = models.BooleanField(default=True)  # доступность товара

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'


    def __str__(self):
        return self.title

class Image(models.Model):
    image = models.ImageField()
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='Product', related_name='image')

    def clean(self):
        if len(Image.objects.filter(product_id=self.product.pk)) >= 8:
            raise ValidationError('The number photos should not exceed 8')


             # """ О нас"""""

class AboutUs(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, max_length=2000)

    class Meta:
        verbose_name = 'AboutUs'
        verbose_name_plural = 'AboutUss'

    def __str__(self):
        return self.name

class ImageUs(models.Model):
    image = models.ImageField()
    about_us = models.ForeignKey(AboutUs, on_delete=models.CASCADE, related_name='image')

    def clean(self):
        if len(Image.objects.filter(product_id=self.about_us.pk)) >= 3:
            raise ValidationError('The number photos should not exceed 3')

                       # """"Коллекция"""

class Collection(models.Model):
    name = models.CharField(max_length=55)
    image = models.ImageField(upload_to='images/Y%/M%/H%',null=False)

    class Meta:
        verbose_name = 'Collection'
        verbose_name_plural = 'Collections'

    def __str__(self):
        return self.name




# class Gallery(models.Model):
#     image = models.ImageField(upload_to='gallery')
#     product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='images')
#
#
# class Stock(models.Model):
#     amount = models.PositiveIntegerField()
#     product = models.ForeignKey('Product', on_delete=models.CASCADE)
#     size = models.ForeignKey('Size', on_delete=models.CASCADE)
#     color = models.ForeignKey('Color', on_delete=models.CASCADE)
#
#     unique_together = ('product', 'size', 'color')

# class ProductItem(models.Model):
#     product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='product_item')
#     price = models.DecimalField(max_digits=10, decimal_places=2)
#     size = models.DecimalField(max_length=8, decimal_places=2)


# class Collection(models.Model):
#     name = models.CharField(max_length=55)
#     image = models.ForeignKey(Gallery, on_delete=models.CASCADE, related_name='image')