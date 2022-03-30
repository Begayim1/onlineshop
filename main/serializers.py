from rest_framework import serializers

from .models import *

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'name', 'image')

class ColorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Color
        fields = ('name', 'color')

class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ('image',)

class ProductSerializer(serializers.ModelSerializer):
    image = ImageSerializer(read_only=True, many=True)
    color = ColorSerializer(read_only=True, many=True)

    class Meta:
        model = Product
        fields = ('id', 'title', 'article', 'color', 'price', 'old_price', 'size', 'fabric', 'material', 'quantity_in_line', 'description', 'image',)

