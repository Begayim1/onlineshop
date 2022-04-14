from django.http import HttpResponseRedirect
from django.shortcuts import render
from rest_framework import request
from rest_framework.decorators import api_view
from rest_framework.response import Response

from  main.models import *
from .serializers import *
from rest_framework.viewsets import ModelViewSet


class OrderListView(ModelViewSet):
    serializer_class = OrderSerializer
    queryset = Order.objects.all()


class CartListView(ModelViewSet):
    serializer_class = CartSerializer
    queryset = Cart.objects.all()

class CartItemListView(ModelViewSet):
    serializer_class = CaetItemSerializer
    queryset = CartItem.objects.all()



# @api_view(['GET'])
# def order(request,id):
#     queryset_cat = Order.objects.get(pk=id)
#     serializer = OrderSerializer(queryset_cat, many=True)
#     return Response(serializer.data)