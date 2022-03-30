from rest_framework.views import APIView
from .models import *
from .serializers import *
from rest_framework.response import Response

class ProductListView(APIView):
    def get(self, request):
        products = Product.objects.all()
        serializer = ProductSerializer(products, many = True)
        return Response(serializer.data)



