from django.http import HttpResponseRedirect
from django.shortcuts import render
from rest_framework import request
from  main.models import *
from .serializers import *

from rest_framework.viewsets import ModelViewSet


class OrderListView(ModelViewSet):
    serializer_class = OrderSerializer
    queryset = Order.objects.all()
