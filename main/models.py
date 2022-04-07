import time

from django.core.exceptions import ValidationError
from django.db import models
from colorful.fields import RGBColorField
from ckeditor.fields import RichTextField


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


class Size(models.Model):
    size = models.CharField(max_length=20)

    class Meta:
        verbose_name = 'Size'
        verbose_name_plural = 'Sizes'

    def __str__(self):
        return self.size


class Product(models.Model):
    title = models.CharField(max_length=100)  # название
    description = RichTextField(blank=True, null=True, max_length=800)  # описание
    article = models.CharField(max_length=55)  # артикл
    fabric = models.CharField(max_length=55, )  # cостав ткани
    material = models.CharField(max_length=55)  # материал
    quantity_in_line = models.PositiveSmallIntegerField(default=0)  # количество в линейке
    price = models.DecimalField(max_digits=10, decimal_places=2)
    old_price = models.PositiveIntegerField(null=True, blank=True)  # старая цена
    discount = models.IntegerField(null=True, blank=True)
    size = models.ManyToManyField(Size, verbose_name=Size)
    # color = models.ManyToManyField(Color, verbose_name=Color, related_name='product')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True)
    hit_of_sales = models.BooleanField(default=False)  # хит продаж
    new = models.BooleanField(default=True)  # новинки
    favorite = models.BooleanField(default=True)

    def __str__(self):
        return self.title

    def discount(self):
        if self.discount and self.old_price:
            self.price = int(self.old_price * (100 - self.discount) / 100)

        else:
            self.price = self.old_price
            self.old_price = 0

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'

        def __str__(self):
            return self.title


class Color(models.Model):
    name = models.CharField(max_length=55)
    color = RGBColorField()
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='Product', related_name='color', null=True)

    def __str__(self):
        return self.name


class Image(models.Model):
    image = models.ImageField()
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='Product', related_name='image')

    # """ О нас"""""


class AboutUs(models.Model):
    name = models.CharField(max_length=100)
    description = RichTextField(blank=True, null=True, max_length=800)

    class Meta:
        verbose_name = 'AboutUs'
        verbose_name_plural = 'AboutUss'

    def __str__(self):
        return self.name


class ImageUs(models.Model):
    image = models.ImageField()
    about_us = models.ForeignKey(AboutUs, on_delete=models.CASCADE, related_name='image')

    # """"Коллекция"""


class Collection(models.Model):
    name = models.CharField(max_length=55)
    image = models.ImageField(upload_to='images/Y%/M%/H%', null=False)

    class Meta:
        verbose_name = 'Collection'
        verbose_name_plural = 'Collections'

    def __str__(self):
        return self.name

        # """ Новости """


class News(models.Model):
    name = models.CharField(max_length=55)
    description = RichTextField(blank=True, null=True, max_length=800)
    image = models.ImageField(upload_to='images/Y%/M%/H%', null=False)

    def __str__(self):
        return self.name


# """Наши преимущества"""

class Advantages(models.Model):
    name = models.CharField(max_length=55)
    description = models.TextField(blank=True, null=True, max_length=800)
    image = models.ImageField(upload_to='images/Y%/M%/H%', null=False)

    def __str__(self):
        return self.name


# """Публичная оферта"""

class PublicOffer(models.Model):
    name = models.CharField(max_length=55)
    description = RichTextField(blank=True, null=True, max_length=800)

    def __str__(self):
        return self.name


# """Помощь"""

class Help(models.Model):
    question = models.CharField(max_length=55)
    answer = models.CharField(max_length=150)

    def __str__(self):
        return self.question


class ImageHelp(models.Model):
    image = models.ImageField()
    help = models.ForeignKey(Help, on_delete=models.CASCADE, related_name='image')


# """гл стр слайдер"""
class Slider(models.Model):
    image = models.ImageField(upload_to='images')
    link = models.URLField(blank=True)


# """Футер"""
class Footer(models.Model):
    SITE = (
        ('WhatsApp', 'WhatsApp'),
        ('Telegram', 'Telegram'),
        ('Instagram', 'Instagram'),
        ('Mail', 'Mail')
    )
    logo = models.ImageField(upload_to='images_f')
    logo_h = models.ImageField(null=True, blank=True, upload_to='image_h')
    description = models.TextField(max_length=200)
    num = models.CharField(max_length=55)
    type = models.CharField(choices=SITE, max_length=55)
    link_num = models.CharField(max_length=150, null=True, blank=True)
    account = models.CharField(max_length=55, null=True, blank=True)

    def save(self, *args, **kwargs):
        if self.type == 'WhatsApp':
            self.link_num = f'https://wa.me/{self.link_num}/'
        elif self.type == 'Telegram':
            self.account = f'https://t.me/{self.account}/'
        elif self.type == 'Instagram':
            self.account = f'https://www.instagram.com/{self.account}/'
        elif self.type == 'Mail':
            self.account = f'https://mail.google.com/{self.account}/'
        super().save(*args, **kwargs)

    def __str__(self):
        return self.description


class ReturnCall(models.Model):
    LINK = (
        ('Whatsapp', 'Whatsapp'),
        ('Telegram', 'Telegram'),
        ('Number', 'Number'),
    )

    status = models.CharField(choices=LINK, max_length=55)
    name = models.CharField(max_length=55)
    num_user = models.CharField(max_length=55)
    return_call = models.BooleanField(default=True)

    def save(self, *args, **kwargs):
        if self.status == 'Whatsapp':
            self.num_user = f'https://wa.me/{self.num_user}/'
        elif self.status == 'Telegram':
            self.num_user = f'https://t.me/{self.num_user}/'
        elif self.status == 'Number':
            self.num_user = f'+996{self.num_user}/'
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class ListOfReferences(models.Model):
    name = models.CharField(max_length=55)
    num = models.CharField(max_length=55)
    created_at = models.DateTimeField(verbose_name='Data', auto_now=True)
    return_call = models.BooleanField(default=True)
    call = models.BooleanField(default=True)


# random_prod = Product.objects.order_by('?')[:4]
