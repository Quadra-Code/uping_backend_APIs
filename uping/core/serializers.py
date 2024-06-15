from rest_framework import serializers
from .models import Country, CategoriesTree, Item, Client, OrderMaster, OrderDetail

class CountriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = ['idCountries', 'name', 'Imgs_idImgs']

class TreeSerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoriesTree
        fields = ['id', 'is_parent', 'level', 'Parent_id']

class ItemsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = [
            'items_id', 'name', 'Tree_id', 'sell_price', 'description',
            'country', 'ingredients', 'how_to_use', 'quantity', 'offer',
            'Countries_idCountries', 'purchase_price', 'unit', 'notes'
        ]

class ClientsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = ['idClients', 'phone_number', 'name', 'Users_user_id']

class OrderMasterSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderMaster
        fields = [
            'idOrderMaster', 'Clients_idClients', 'paid', 'datetime',
            'state', 'address', 'order_total', 'notes'
        ]

class OrderDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderDetail
        fields = ['idOrderDetail', 'OrderMaster_idOrderMaster', 'Items_items_id', 'quantity', 'notes', 'detail_price']
