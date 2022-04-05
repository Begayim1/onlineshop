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

    title = models.CharField(max_length=100) #название
    description = RichTextField(blank=True, null=True, max_length=800) #описание
    # created = models.DateTimeField(default=True)  # хранит дату когда был создан объект.
    article = models.CharField(max_length=55) #артикл
    fabric = models.CharField(max_length=55, ) #cостав ткани
    material = models.CharField(max_length=55) #материал
    quantity_in_line = models.PositiveSmallIntegerField(default=0) #количество в линейке
    price = models.DecimalField(max_digits=10, decimal_places=2)
    old_price = models.PositiveIntegerField(null=True, blank=True) #старая цена
    discount = models.IntegerField(null=True, blank=True)
    size = models.ManyToManyField(Size, verbose_name=Size)
    # color = models.ManyToManyField(Color, verbose_name=Color, related_name='product')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True)
    hit_of_sales = models.BooleanField(default=False) #хит продаж
    new = models.BooleanField(default=True) #новинки
    favorite = models.BooleanField(default=True)

    def __str__(self):
        return self.title

    def discount(self):
        if self.discount and self.old_price:
            self.price = int(self.old_price * (100 - self.discount) / 100 )

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
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='Product', related_name='color')

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
    image = models.ImageField(upload_to='images/Y%/M%/H%',null=False)

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



class Slider(models.Model):
    image = models.ImageField(upload_to='images')
    link = models.URLField(blank=True)



# """Футер"""
class Type(models.Model):
    name = models.CharField(max_length=55, unique=True)

    def __str__(self):
        return self.name

class Footer(models.Model):
    logo = models.ImageField(upload_to='images_f')
    logo = models.ImageField(null=True, blank=True, upload_to='image_h')
    description = models.TextField(max_length=200)
    num = models.PositiveIntegerField()
    type = models.ForeignKey(Type, on_delete=models.DO_NOTHING)
    link = models.URLField(max_length=150, null=True, blank=True)
    number = models.PositiveIntegerField()
    message = models.CharField(max_length=55, null=True, blank=True)

    def save(self, *args, **kwargs):
        if self.type.name == 'WhatsApp':
            self.link = f'https://wa.me/{self.number}/'
        elif self.type.name == 'Telegram':
            self.link = f'https://t.me/{self.number}/'
        elif self.type.name == 'Instagram':
            self.link = f'https://www.instagram.com/{self.message}/'
        elif self.type.name == 'Mail':
            self.link = f'https://mail.google.com/{self.message}/'
        super().save(*args, **kwargs)

    def __str__(self):
        return self.description

#     logo = models.ImageField('Логотип', upload_to='images_footer')
#     description = models.TextField('Текстовая информация', max_length=1500)
#     num = models.PositiveIntegerField('Номер в хедере')
#     type = models.CharField('Тип', max_length=100, choices=social_media)
#     link = models.URLField('Ссылка')
#     phone1 = models.CharField('Номера телефона 1' , max_length=20)
#     phone2 = models.CharField('Номера телефона 2', max_length=20, blank=True)
#     phone3 = models.CharField('Номера телефона 3', max_length=20, blank = True)
#     gmail = models.CharField('Почта', max_length=100)




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