from rest_framework import generics
from .serializers import OrderModelSerializer, OrderItemSerializer
from orders.models import Order,OrderItems
from rest_framework import permissions
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.parsers import JSONParser




class OrderItemsView(viewsets.ModelViewSet):
    queryset = OrderItems.objects.all()
    serializer_class = OrderItemSerializer

class OrdersCreateView(APIView):



    def post(self, request, format=None):
        json_data = JSONParser().parse(request)
        print(json_data.get("items"))
        return Response({"HELLO":"HELLO"})
