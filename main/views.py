from django.http import Http404
from rest_framework.decorators import api_view, action
from rest_framework.pagination import PageNumberPagination
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from .models import *
from .serializers import *
from rest_framework.response import Response
from  rest_framework import filters

class MyPaginationClass(PageNumberPagination):
    page_size = 2
    max_page_size = 3

# """Товары"""

class ProductListView(APIView):
    def get(self, request):
        products = Product.objects.all()
        serializer = ProductSerializer(products, many = True)
        return Response(serializer.data)


# """О нас"""
class AboutUsListView(APIView):
    def get(self, request):
        about_us = AboutUs.objects.all()
        serializer = AboutUsSerializer(about_us, many=True)
        return Response(serializer.data)


class ProductsListView(ModelViewSet):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
    pagination_class = MyPaginationClass
    filter_backends = (filters.SearchFilter,)
    search_fields = ['title']


# """Колекции"""
class CollectionListView(ModelViewSet):
    serializer_class = CollectionSerializer
    queryset = Collection.objects.all()
    pagination_class = MyPaginationClass

# """Новсти"""
class NewsListView(ModelViewSet):
    serializer_class = NewsSerializer
    queryset = News.objects.all()
    pagination_class = MyPaginationClass

# """похожие продукты"""
@api_view(['GET'])
def similar_product(request, pk):
    category = Category.objects.get(id=pk)
    queryset = Product.objects.all().filter(category=category)[0:5]
    serializer = ProductSerializer(queryset, many=True)
    return Response(serializer.data)

# """Список товаров"""
@api_view(['GET'])
def list_product(request, pk):
    category = Category.objects.get(id=pk)
    queryset = Product.objects.all().filter(category=category)[0:12]
    serializer = ProductSerializer(queryset, many=True)
    return Response(serializer.data)

# """Новые Продукты со статусом"""
@api_view(['GET'])
def new_product(request, pk):
    category = Category.objects.get(id=pk)
    queryset = Product.objects.all().filter(new=True)[0:5]
    serializer = ProductSerializer(queryset, many=True)
    return Response(serializer.data)

# """Футер"""
@api_view(['GET'])
def footer(request):
    obj = Footer.objects.all()
    serializer = FooterSerializer(obj, many=True)
    return Response(serializer.data)

# """Глав стр Хит Продаж со стат"""
@api_view(['GET'])
def hit_of_sales(request):
    queryset = Product.objects.all().filter(hit_of_sales=True)[0:8]
    serializer = ProductSerializer(queryset, many=True)
    return Response(serializer.data)

# """Глав стр Со статусом Новинки"""
@api_view(['GET'])
def new(request):
    queryset = Product.objects.all().filter(new=True)[0:4]
    serializer = ProductSerializer(queryset, many=True)
    return Response(serializer.data)

# """Главная стр колекции"""
@api_view(['GET'])
def collection(request,id):
    queryset_cat = Category.objects.get(pk=id)
    queryset = Product.objects.all().filter(category=queryset_cat)[0:4]
    serializer = ProductSerializer(queryset, many=True)
    return Response(serializer.data)

# """Главная стр преимущества"""
@api_view(['GET'])
def advantages(request):
    queryset = Advantages.objects.all().filter()[0:4]
    serializer = AdvantagesSerializers(queryset, many=True)
    return Response(serializer.data)

# @api_view(['GET'])
# def product_search(request):
#     obj = []
#     number = models.Category.objects.all().count()
#     if number >= 5:
#         for i in models.Category.objects.all().values_list('id')[0:5]:
#             if models.Product.objects.all().filter(category=i).first() is None:
#                 pass
#             else:
#                 obj.append(models.Product.objects.all().filter(category=i).first())
#     else:
#         for i in models.Category.objects.all().values_list('id')[0:number]:
#             if models.Product.objects.all().filter(category=i).first() is None:
#                 pass
#             else:
#                 obj.append(models.Product.objects.all().filter(category=i).first())
#     serializer = serializers.ProductSerializer(obj, many=True)
#     return Response(serializer.data)

"""избранное"""
@api_view(['GET'])
def favorite(request):
    queryset = Product.objects.all().filter(favorite=True)[0:12]
    serializer = ProductSerializer(queryset, many=True)
    return Response(serializer.data)

# """гл стр слайдер"""
class SliderListView(ModelViewSet):
    queryset = Slider.objects.all()
    serializer_class = SliderSerializer

# """Публичная оферта"""
class PublicOfferListView(ModelViewSet):
    serializer_class = PublicOfferSerializer
    queryset = PublicOffer.objects.all()

# """Помощь"""
class HelpListView(APIView):
    def get(self, request):
        help = Help.objects.all()
        serializer_class = HelpSerializer(help, many=True)
        return Response(serializer_class.data)


class ReturnCallListView(ModelViewSet):
    serializer_class = ReturnCallSerializer
    queryset = ReturnCall.objects.all()




