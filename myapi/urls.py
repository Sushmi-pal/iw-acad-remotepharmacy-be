from django.urls import include, path
from rest_framework import routers
from . import views
from rest_framework.authtoken.views import obtain_auth_token

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
# router.register(r'products', views.ProductViewSet)
from django.urls import path
from datahandle.views import info_view,info_view_cat,info_product_view,info_view_prod,info_view_prodindividual
from .generic_views import UserRegisterCreateAPIView,\
    ProductsListView,ProductRetrieveUpdateView,UserLoginCreateView,UserLogoutView


urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('categories/<int:pk>/',info_view_cat),
    path('categories/',info_view),
    path('products/',info_product_view),
    path('products/<int:pk>',info_view_prodindividual),
    # path('login/',obtain_auth_token),
    path('register/',UserRegisterCreateAPIView.as_view()),
    path('generic/products/',ProductsListView.as_view()),
    # path('generic/products/update/<int:pk>',ProductRetrieveUpdateView.as_view()),
    path('generic/products/updatedetail/<int:pk>',ProductRetrieveUpdateView.as_view()),
    path('login/',UserLoginCreateView.as_view()),
    path('logout/',UserLogoutView.as_view())
]
