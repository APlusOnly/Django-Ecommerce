from django.urls import path
from . import views
from .views import (
    CategoryDetailView,
)

urlpatterns = [
    path('', views.home, name='home'),
    path('departments/', views.departments, name='departments'),
    path('category/<int:pk>/', CategoryDetailView.as_view(), name='category-view'),
    path('my_account/', views.my_account, name='my_account'),
    path('cart/', views.my_cart, name='my_cart'),
    path('log_in/', views.log_in, name='log_in'),
    path('item/<int:pk>/', views.item_view, name='item-view')
]