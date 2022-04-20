from random import random, choice

from django.http import Http404
from rest_framework.decorators import api_view, action
from rest_framework.pagination import PageNumberPagination
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from .models import *
from .serializers import *
from rest_framework.response import Response
from rest_framework import filters, status
from .models import *

''' Пагинация '''


class MyPaginationClass(PageNumberPagination):
    page_size = 8
    max_page_size = 5



    ''' О нас '''


class AboutUsListView(APIView):
    def get(self, request):
        about_us = AboutUs.objects.all()
        serializer = AboutUsSerializer(about_us, many=True)
        return Response(serializer.data)


class ColorListView(ModelViewSet):
    serializer_class = ColorSerializer
    queryset = Color.objects.all()

    ''' Товары '''


class ProductsListView(ModelViewSet):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
    pagination_class = MyPaginationClass
    filter_backends = (filters.SearchFilter,)
    search_fields = ['title']

    ''' Новости '''


class NewsListView(ModelViewSet):
    serializer_class = NewsSerializer
    queryset = News.objects.all()
    pagination_class = MyPaginationClass

    ''' 
    Похожие продукты 
    '''


@api_view(['GET'])
def similar_product(request, pk):
    category = Category.objects.get(id=pk)
    queryset = Product.objects.all().filter(category=category)[0:5]
    serializer = ProductSerializer(queryset, many=True)
    return Response(serializer.data)


'''
 Список товаров
'''


@api_view(['GET'])
def list_product(request, pk):
    category = Category.objects.get(id=pk)
    queryset = Product.objects.all().filter(category=category)[0:12]
    serializer = ProductSerializer(queryset, many=True)
    return Response(serializer.data)


'''
 Новые Продукты со статусом
'''


@api_view(['GET'])
def new_product(request, pk):
    category = Category.objects.get(id=pk)
    queryset = Product.objects.all().filter(new=True)[0:5]
    serializer = ProductSerializer(queryset, many=True)
    return Response(serializer.data)


''' Футер '''


@api_view(['GET'])
def footer(request):
    obj = Footer.objects.all()
    serializer = FooterSerializer(obj, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def footer(request):
    if request.method == 'GET':
        queryset = Footer.objects.all()
        serializer = FooterSerializer(queryset, many=True)
        return Response(serializer.data)


''' Глав стр Хит Продаж со стат '''


@api_view(['GET'])
def hit_of_sales(request):
    queryset = Product.objects.all().filter(hit_of_sales=True)[0:8]
    serializer = ProductSerializer(queryset, many=True)
    return Response(serializer.data)


"""Глав стр Со статусом Новинки"""


@api_view(['GET'])
def new(request):
    queryset = Product.objects.all().filter(new=True)[0:4]
    serializer = ProductSerializer(queryset, many=True)
    return Response(serializer.data)


''' Главная стр преимущества'''


@api_view(['GET'])
def advantages(request):
    queryset = Advantages.objects.all().filter()[0:4]
    serializer = AdvantagesSerializers(queryset, many=True)
    return Response(serializer.data)


''' Избранное '''


@api_view(['GET'])
def favorite(request):
    queryset = Product.objects.all().filter(favorite=True)[0:12]
    serializer = ProductSerializer(queryset, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def product_search(request):
    obj = []
    number = Category.objects.all().count()
    if number >= 5:
        for i in Category.objects.all().values_list('id')[0:5]:
            if Product.objects.order_by('?').filter(category_id=i).first is None:
                pass
            else:
                obj.append(choice(Product.objects.order_by('?').filter(category_id=i)))
    else:
        for i in Category.objects.all().values_list('id')[0:number]:
            if Product.objects.order_by('id').filter(category_id=i).first() is None:
                pass
            else:
                obj.append(choice(Product.objects.order_by('?').filter(category_id=i)))
    serializer = ProductSerializer(obj, many=True)
    return Response(serializer.data)


''' гл стр слайдер '''


class SliderListView(ModelViewSet):
    queryset = Slider.objects.all()
    serializer_class = SliderSerializer


''' Публичная оферта '''


@api_view(['GET'])
def public_offer(request):
    queryset = PublicOffer.objects.all()
    serializer = PublicOfferSerializer(queryset, many=True)
    return Response(serializer.data)


''' Помощь '''


class HelpListView(ModelViewSet):
    serializer_class = HelpSerializer
    queryset = Help.objects.all()

    ''' 
    Обратный званок 
    '''


class ListListView(ModelViewSet):
    serializer_class = ListOfSerializer
    queryset = ListOfReferences.objects.all()
