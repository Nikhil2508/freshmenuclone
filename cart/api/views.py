import json
from rest_framework import generics
from cart.models import Cart, CartItem
from .serializers import CartSerializer, CartItemSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from products.models import Product
from django.shortcuts import get_object_or_404
from django.conf import settings
from django.contrib.auth import get_user_model
from django.core import serializers

User  = get_user_model()



class CartListView(generics.ListAPIView):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer



class CartDetailAPIView(generics.RetrieveAPIView):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer



class CartCreateAPIView(APIView):




    def post(self, request):
        cart_id = request.session.get("cart_id")
        data = json.loads(request.body)
        items = data['items']
        if not items:
            print("List empty")
        else:
            if cart_id == None:
                cart = Cart()
                cart.user = User.objects.get(id=data['user'])
                cart.save()
                cart_id = cart.id
                request.session['cart_id'] = cart_id
            else:
                cart = Cart.objects.get(id=cart_id)
            for item in items:
                cart_item = CartItem()
                cart_item.cart = cart
                cart_item.item = get_object_or_404(Product.objects.all(),pk=item['itemid'])
                cart_item.quantity = item['quantity']
                cart_item.save()
                cart.items.add(cart_item)
            cart.save()
            # data = serializers.serialize('json', [cart,])
            # struct = json.loads(data)
            # data = json.dumps(struct[0])
            data = CartSerializer(Cart.objects.get(id=cart.id)).data
            # data2 = CartItemSerializer(cart.cartitem_set.all()).data
            # print (d)
        return Response({'data':data})
