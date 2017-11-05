from rest_framework import serializers
from products.models import Product, ProductCategories




class ProductCategoryModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductCategories
        fields = ("__all__")


class ProductModelSerializer(serializers.ModelSerializer):
    category = ProductCategoryModelSerializer(read_only=True, many=True)
    class Meta:
        model = Product
        fields = ("__all__")
