from django.urls import path,include
from .views import LoginView,RegisterView, MainView,LogoutView
app_name='users'
urlpatterns=[
    path('login/', LoginView,name='login'),
    path('register/',RegisterView,name='register'),
    path('main/',MainView,name='main'),
    path('logout/',LogoutView,name='logout'),

]