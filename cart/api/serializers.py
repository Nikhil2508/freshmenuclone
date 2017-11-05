from rest_framework import serializers
from cart.models import Cart, CartItem



class CartItemSerializer(serializers.ModelSerializer):
    itemid = serializers.SerializerMethodField()
    itemprice = serializers.SerializerMethodField()
    class Meta:
        model = CartItem
        fields = [
            'itemid',
            'itemprice',
            'quantity'
        ]

    def get_itemid(self, obj):
        return obj.item.id
    def get_itemprice(self, obj):
        return obj.item.price


class CartSerializer(serializers.ModelSerializer):
    items = CartItemSerializer(read_only=True, many=True)
    class Meta:
        model = Cart
        fields = [
            'id',
            'user',
            'items',
            'timestamp',
        ]
