from django.urls import path, include
from rest_framework import routers
from .views import info_view, info_view_cat, info_product_view, info_view_prod,\
    info_view_prodindividual, add_to_cart, remove_from_cart
from . import views
router = routers.DefaultRouter()
router.register(r'cart', views.CartViewSet)
router.register(r'orders', views.OrderViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('dh/<int:pk>/', info_view_cat),
    path('dh/', info_view),
    path('dp/', info_product_view),
    path('dp/<int:pk>', info_view_prodindividual),
    path('add/<slug>', views.add_to_cart, name='add-to-cart'),
    path('remove/<slug>', views.remove_from_cart, name='remove_from_cart'),

]