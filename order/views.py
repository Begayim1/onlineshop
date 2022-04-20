from django.http import HttpResponseRedirect
from django.shortcuts import render
from rest_framework import request
from rest_framework.decorators import api_view
from rest_framework.response import Response

from main.models import *
from .serializers import *
from rest_framework.viewsets import ModelViewSet


class OrderListView(ModelViewSet):
    serializer_class = OrderSerializer
    queryset = Order.objects.all()


class CartListView(ModelViewSet):
    serializer_class = CartSerializer
    queryset = Cart.objects.all()


class CartItemListView(ModelViewSet):
    serializer_class = CartItemSerializer
    queryset = CartItem.objects.all()

    def save(self, *args, **kwargs):
        self.price_q = self.product.old_price * self.quan_sum
        self.quan_sum = self.product.quantity_in_line * self.quantity
        self.rebate = (self.product.old_price - self.product.price) * self.quan_sum
        self.sum_r = self.product.price * self.quan_sum
        super().save(*args, **kwargs)
