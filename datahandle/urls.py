from django.urls import path
from .views import info_view,info_view_cat,info_product_view,info_view_prod,info_view_prodindividual
urlpatterns=[
    path('dh/<int:pk>/',info_view_cat),
    path('dh/',info_view),
    path('dp/',info_product_view),
    path('dp/<int:pk>',info_view_prodindividual)


]