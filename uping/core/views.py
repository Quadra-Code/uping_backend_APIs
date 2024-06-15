from django.shortcuts import render
from rest_framework import viewsets
from .models import Country, Item, Client, OrderMaster, OrderDetail
from .serializers import CountriesSerializer, ItemsSerializer, ClientsSerializer, OrderMasterSerializer, OrderDetailSerializer

# Create your views here.

class CountriesViewSet(viewsets.ModelViewSet):
    queryset = Country.objects.all()
    serializer_class = CountriesSerializer

class ItemsViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemsSerializer

class ClientsViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientsSerializer

class OrderMasterViewSet(viewsets.ModelViewSet):
    queryset = OrderMaster.objects.all()
    serializer_class = OrderMasterSerializer

class OrderDetailViewSet(viewsets.ModelViewSet):
    queryset = OrderDetail.objects.all()
    serializer_class = OrderDetailSerializer
