import time

from django.core.exceptions import ValidationError
from django.db import models
from colorful.fields import RGBColorField
from ckeditor.fields import RichTextField

''' Товары '''


class Category(models.Model):
    name = models.CharField(max_length=55,
                            unique=True)
    image = models.ImageField()

    class Meta:
        ordering = ('name',)
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name




class Product(models.Model):
    title = models.CharField(max_length=100)  # название
    description = RichTextField(blank=True,
                                null=True,
                                max_length=800)  # описание
    article = models.CharField(max_length=55)  # артикл
    fabric = models.CharField(max_length=55, )  # cостав ткани
    material = models.CharField(max_length=55)  # материал
    quantity_in_line = models.PositiveSmallIntegerField(default=1)  # количество в линейке
    price = models.DecimalField(max_digits=10,
                                decimal_places=2)
    old_price = models.PositiveIntegerField(null=True,
                                            blank=True)  # старая цена
    discount = models.IntegerField(null=True,
                                   blank=True)
    size_for_product = models.CharField(max_length=55, null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE,
                                 null=True, blank=True)
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
    product = models.ForeignKey(Product,
                                on_delete=models.CASCADE,
                                verbose_name='Product',
                                related_name='color',
                                null=True)

    def __str__(self):
        return self.name


class Image(models.Model):
    image = models.ImageField()
    product = models.ForeignKey(Product,
                                on_delete=models.CASCADE,
                                verbose_name='Product',
                                related_name='image')

    ''' О нас '''


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



    ''' Новости '''


class News(models.Model):
    name = models.CharField(max_length=55)
    description = RichTextField(blank=True, null=True, max_length=800)
    image = models.ImageField(upload_to='images/Y%/M%/H%', null=False)

    def __str__(self):
        return self.name

    ''' 
    Наши преимущества 
    '''


class Advantages(models.Model):
    name = models.CharField(max_length=55)
    description = models.TextField(blank=True, null=True, max_length=800)
    image = models.ImageField(upload_to='images/Y%/M%/H%', null=False)

    def __str__(self):
        return self.name

    ''' 
    Публичная оферта 
    '''


class PublicOffer(models.Model):
    name = models.CharField(max_length=55)
    description = RichTextField(blank=True, null=True, max_length=800)

    def __str__(self):
        return self.name

    ''' Помощь '''


class Help(models.Model):
    question = models.CharField(max_length=55)
    answer = models.CharField(max_length=150)

    def __str__(self):
        return self.question

class ImageHelp(models.Model):
    image = models.ImageField()


    ''' 
    гл стр слайдер 
    '''


class Slider(models.Model):
    image = models.ImageField(upload_to='images')
    link = models.URLField(blank=True)

    ''' Футер '''


class Footer(models.Model):

    logo = models.ImageField(upload_to='images_f')
    logo_h = models.ImageField(null=True, blank=True,
                               upload_to='image_h')
    description = models.TextField(max_length=200)
    num = models.CharField(max_length=55)
    link_w = models.CharField(max_length=150,
                                null=True, blank=True)
    account_t = models.CharField(max_length=55,
                               null=True, blank=True)
    account_in = models.CharField(max_length=55,
                                 null=True, blank=True)
    email = models.CharField(max_length=55,
                             null=True, blank=True)

    def save(self, *args, **kwargs):

        self.link_num = f'https://wa.me/{self.link_w}/'
        self.account = f'https://t.me/{self.account_t}/'
        self.account = f'https://www.instagram.com/{self.account_in}/'
        self.account = f'https://mail.google.com/{self.email}/'
        super().save(*args, **kwargs)

    def __str__(self):
        return self.description


    ''' 
    Список обращений 
    '''


class ListOfReferences(models.Model):
    Coll = (
        ('Yes', 'Yes'),
        ('No', 'No')
    )
    name = models.CharField(max_length=55)
    num = models.CharField(max_length=55)
    type = models.CharField(max_length=55, null=True, blank=True, verbose_name='Тип Обращения')
    date = models.DateTimeField(editable=True, auto_now_add=True)
    return_call = models.CharField(choices=Coll, max_length=55, default='No')

