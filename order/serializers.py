from rest_framework import serializers
from main.models import *
from .models import *
from main.serializers import ProductSerializer


class OrderSerializer(serializers.ModelSerializer):
    product = ProductSerializer()
    class Meta:
        model = Order
        fields = ('id','product')
