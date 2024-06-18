from django.contrib import admin
from .models import CategoriesTree, Item, OrderMaster, OrderDetail, ItemImg, Client, ClientAddress, ClientPhone, Country
# Register your models here.
admin.site.register(
    [
        CategoriesTree,
        Country,
    ]
)