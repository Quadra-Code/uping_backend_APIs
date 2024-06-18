from django.shortcuts import render
from rest_framework import viewsets
from .models import Country, Item, Client, OrderMaster, OrderDetail
from .serializers import CountriesSerializer, ItemsSerializer, ClientsSerializer, OrderMasterSerializer, OrderDetailSerializer, CategoriesTree
from .utils import get_categories_tree_list
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.core.exceptions import ObjectDoesNotExist
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

@api_view(['GET'])
def get_categories_tree(request):
    parents_queryset = CategoriesTree.objects.filter(level=0).order_by('id')
    data = get_categories_tree_list(parents=parents_queryset)
    return Response(data, status=status.HTTP_200_OK)