from django.db import models

from main.models import *


class Cart(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='cart_product', blank=True)
    quantity = models.PositiveIntegerField(default=1)
    price_q = models.IntegerField(default=True, null=True, blank=True, verbose_name='Cтоимость')
    quan_sum = models.IntegerField(default=True, null=True, blank=True, verbose_name='Общ Количество:')
    rebate = models.IntegerField(default=True, null=True, blank=True, verbose_name='Скидка')
    sum_r = models.IntegerField(default=True, null=True, blank=True, verbose_name='Итого')

    def save(self, *args, **kwargs):
        self.price_q = self.product.old_price * self.quan_sum
        self.quan_sum = self.product.quantity_in_line * self.quantity
        self.rebate = (self.product.old_price - self.product.price) * self.quan_sum
        self.sum_r = self.product.price * self.quan_sum
        super().save(*args, **kwargs)


class CartItem(models.Model):
    cart = models.ManyToManyField(Cart, related_name='related_cart', blank=True)
    price = models.IntegerField(null=True, blank=True, default=0)
    quantity = models.PositiveIntegerField(null=True, blank=True, default=0)
    sum = models.IntegerField(null=True, blank=True, default=0)
    sum_quantity = models.IntegerField(null=True, blank=True, default=0)
    discounts = models.IntegerField(null=True, blank=True, default=0)
    total = models.IntegerField(null=True, blank=True, default=0)

    def save(self, *args, **kwargs):
        if self.id:
            self.quantity = sum([cproduct.quantity for cproduct in self.cart.all()])
            self.sum_quantity = sum([c.quan_sum for c in self.cart.all()])
            self.price = sum([c.price_q for c in self.cart.all()])
            self.discounts = sum([c.rebate for c in self.cart.all()])
            self.total = sum([c.sum_r for c in self.cart.all()])
        super().save(*args, **kwargs)

    def get_cost(self):
        if self.id:
            return self.price * self.quantity


class Order(models.Model):
    STATUS = (
        ('New', 'New'),
        ('Decorated', 'Decorated'),
        ('Cancelled', 'Cancelled'),
    )
    name = models.CharField(max_length=55)
    last_name = models.CharField(max_length=60)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='cart')
    phone = models.CharField(max_length=13)
    address = models.TextField()
    city = models.CharField(max_length=100)
    email = models.EmailField()
    created_at = models.DateTimeField(verbose_name='Data', auto_now=True)
    status = models.CharField(choices=STATUS, max_length=55, null=True, default='New')
    description = models.CharField(max_length=55, null=True, blank=True)
    cart = models.ManyToManyField(CartItem, related_name='items')

    def save(self, *args, **kwargs):
        if self.status == '':
            self.status = f'New'
        elif self.status == 'New':
            self.description = f'Product {self.status}'
        elif self.status == 'Decorated':
            self.description = f'Product {self.status}'
        elif self.status == 'Cancelled':
            self.description = f'Product {self.status}'
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

    def __str__(self):
        return 'Order {}'.format(self.id)

    def get_total_cost(self):
        return sum(item.get_cost() for item in self.items.all())


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')

    def __str__(self):
        return '{}'.format(self.id)
