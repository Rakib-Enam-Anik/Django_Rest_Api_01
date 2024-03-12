from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import User, Order
from .serializers import UserSerializer, OrderSerializer

# Create your views here.

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class OrderViewSet(viewsets.ModelViewSet):
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated,]
    
    def get_queryset(self):
           queryset = Order.objects.all()
           id = self.request.query_params.get('id', None)
           if id is not None:
               queryset = queryset.filter(user__id=id)
           return queryset
    
