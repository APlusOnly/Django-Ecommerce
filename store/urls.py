from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('departments/', views.departments, name='departments'),
    path('my_account/', views.my_account, name='my_account'),
    path('my_cart/', views.my_cart, name='my_cart'),
    path('log_in/', views.log_in, name='log_in'),
]