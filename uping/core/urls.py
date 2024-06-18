from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import CountriesViewSet, ItemsViewSet, ClientsViewSet, OrderMasterViewSet, OrderDetailViewSet, get_categories_tree

# router = DefaultRouter()
# router.register(r'countries', CountriesViewSet)
# router.register(r'items', ItemsViewSet)
# router.register(r'clients', ClientsViewSet)
# router.register(r'order_master', OrderMasterViewSet)
# router.register(r'order_detail', OrderDetailViewSet)

urlpatterns = [
    # path('', include(router.urls)),
    path('get-categories', get_categories_tree, name='get_categories_api'),
]
