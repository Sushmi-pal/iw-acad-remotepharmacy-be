from django.urls import include, path
from rest_framework import routers
from . import views
from rest_framework.authtoken.views import obtain_auth_token

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
# router.register(r'products', views.ProductViewSet)
from django.urls import path
from datahandle.views import info_view,info_view_cat,info_product_view,info_view_prod,info_view_prodindividual
from .generic_views import (UserRegisterCreateAPIView,CategoryRetrieveView,
                            ProductsListView,ProductRetrieveView,UserLoginCreateView,
                            UserLogoutView, ProductCreateAPIView,CategoryCreateAPIView,CategoryListView)
from .views import product_delete,product_update,category_delete,userprofile_update
    




urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('users/update/<int:pk>',userprofile_update),
    path('categories/<int:pk>/',info_view_cat),
    path('categories/',CategoryListView.as_view()),
    path('categories/create/',CategoryCreateAPIView.as_view()),
    path('categories/delete/<int:pk>',category_delete),
    path('products/',info_product_view),
    path('products/<int:pk>',info_view_prodindividual),
    path('register/',UserRegisterCreateAPIView.as_view()),
    path('generic/products/',ProductsListView.as_view()),
    path('generic/products/create/',ProductCreateAPIView.as_view()),
    path('generic/products/detail/<int:pk>',ProductRetrieveView.as_view()),
    path('generic/products/delete/<int:pk>',product_delete),
    path('generic/products/update/<int:pk>',product_update),
    # path('generic/products/update/partial/<int:pk>',product_partial_update),
    path('login/',UserLoginCreateView.as_view()),
    path('logout/',UserLogoutView.as_view()),
    # path('users/update/<int:pk>',UserUpdateInfoView.as_view())

    ]
