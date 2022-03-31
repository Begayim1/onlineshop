from rest_framework.pagination import PageNumberPagination
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from .models import *
from .serializers import *
from rest_framework.response import Response

class MyPaginationClass(PageNumberPagination):
    page_size = 2
    max_page_size = 3


class ProductListView(APIView):
    def get(self, request):
        products = Product.objects.all()
        serializer = ProductSerializer(products, many = True)
        return Response(serializer.data)

class AboutUsListView(APIView):
    def get(self, request):
        about_us = AboutUs.objects.all()
        serializer = AboutUsSerializer(about_us, many=True)
        return Response(serializer.data)



class CollectionListView(ModelViewSet):
    serializer_class = CollectionSerializer
    queryset = Collection.objects.all()
    pagination_class = MyPaginationClass

class NewsListView(ModelViewSet):
    serializer_class = NewsSerializer
    queryset = News.objects.all()
    pagination_class = MyPaginationClass

    # def get(self, request):
    #     collection = Collection.objects.all()
    #     serializer = CollectionSerializer(collection, many=True)
    #     return Response(serializer.data)




