from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('departments/', views.departments, name='departments'),
    path('category/<int:pk>/', views.category_view, name='category-view'),
    path('cart/', views.my_cart, name='my_cart'),
    path('log_in/', views.log_in, name='log_in'),
    path('item/<int:pk>/', views.item_view, name='item-view')
]