from ckeditor_uploader.widgets import CKEditorUploadingWidget
from rest_framework import serializers

from .models import *
from order.serializers import *
from order.models import *

''' Товары '''


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
    color = ColorSerializer(many=True)
    image = ImageSerializer(many=True)
    discount = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = '__all__'

    def get_discount(self, obj):
        discount = 100 - (obj.price * 100 // obj.old_price) if obj.old_price else 0
        return discount

    ''' О нас '''


class ImageUsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImageUs
        fields = ('image',)


class AboutUsSerializer(serializers.ModelSerializer):
    image = ImageUsSerializer(read_only=True, many=True)

    class Meta:
        model = AboutUs
        fields = ('name', 'description', 'image',)

    ''' Наши преимущества '''


class AdvantagesSerializers(serializers.ModelSerializer):
    class Meta:
        model = Advantages
        fields = '__all__'



    ''' Новости '''


class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = ('id', 'name', 'description', 'image',)

    ''' 
    Публичная оферта 
    '''


class PublicOfferSerializer(serializers.ModelSerializer):
    class Meta:
        model = PublicOffer
        fields = '__all__'

    ''' Помощь '''


class ImageHelpSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImageHelp
        fields = ('image',)

class HelpSerializer(serializers.ModelSerializer):
    image = ImageHelpSerializer(read_only=True, many=True)
    class Meta:
        model = Help
        fields = ('question', 'answer', 'image',)

    ''' Футер '''


class FooterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Footer
        fields = '__all__'

    ''' 
    гл стр слайдер 
    '''


class SliderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Slider
        fields = '__all__'

    ''' 
    Обратный званок 
    '''


class ListOfSerializer(serializers.ModelSerializer):
    class Meta:
        model = ListOfReferences
        fields = '__all__'
