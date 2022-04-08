from django.db import models

from main.models import Product


class Order(models.Model):
    STATUS = (
        ('New', 'New'),
        ('Decorated', 'Decorated'),
        ('Cancelled', 'Cancelled'),
    )
    name = models.CharField(max_length=55)
    last_name = models.CharField(max_length=60)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='orders')
    phone = models.CharField(max_length=13)
    address = models.TextField()
    city = models.CharField(max_length=100)
    email = models.EmailField()
    created_at = models.DateTimeField(verbose_name='Data', auto_now_add=True)
    status = models.CharField(choices=STATUS, max_length=55, null=True, default='New')
    description = models.CharField(max_length=55,null=True, blank=True)

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
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='order_items')
    price = models.DecimalField(max_digits=10, decimal_places=2,)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return '{}'.format(self.id)

    def clean(self):
        products = Product.objects.filter(order_items=self)
        print(products)

