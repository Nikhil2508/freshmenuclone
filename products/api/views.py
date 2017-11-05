from rest_framework import generics
from .serializers import ProductModelSerializer, ProductCategoryModelSerializer
from products.models import Product, ProductCategories
from rest_framework import permissions
from rest_framework import viewsets
from rest_framework.response import Response


class ProductListView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductModelSerializer
    permission_classes = [permissions.AllowAny]


class ProductCategoryViewSet(viewsets.ModelViewSet):
    queryset = ProductCategories.objects.filter(active=True)
    serializer_class = ProductCategoryModelSerializer
    permission_classes = [permissions.AllowAny]

    def list(self, request):
        queryset = self.get_queryset()
        serializer = ProductCategoryModelSerializer(queryset, many=True)
        if serializer.data:
            return Response({"response":serializer.data,"status":"SUCCESS","message":"Successfull"})
        else:
            return Response({"response":[],"status":"NO RESULT","message":"No result"})

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductModelSerializer

    def list(self, request):
        queryset = Product.objects.filter(category__id__iexact=1)
        serializer = ProductModelSerializer(queryset, many=True)
        if serializer.data:
            return Response({"response":serializer.data,"status":"SUCCESS","message":"Successfull"})
        else:
            return Response({"response":[],"status":"NO RESULT","message":"No result"})
