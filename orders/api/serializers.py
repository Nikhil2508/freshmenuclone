from rest_framework import serializers
from orders.models import Order, OrderItems
from products.api.serializers import ProductModelSerializer


class OrderItemSerializer(serializers.ModelSerializer):
    def __init__(self, *args, **kwargs):
        many = kwargs.pop('many', True)
        super(OrderItemSerializer, self).__init__(many=many, *args, **kwargs)

    class Meta:
        model = OrderItems
        fields=("__all__")



class OrderModelSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(read_only=True, many=True)
    class Meta:
        model = Order
        fields = [
        'user',
        'items',
        ]
