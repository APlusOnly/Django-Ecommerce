from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('departments/', views.departments, name='departments'),
    path('category/<int:pk>/', views.category_view, name='category-view'),
    path('cart/', views.my_cart, name='my-cart'),
    path('item/<int:pk>/', views.item_view, name='item-view'),
    path('wishlist/<int:pk>/', views.add_wishlist, name='add-wishlist'),
    path('wishlist/remove/<int:pk>/', views.remove_wishlist, name='remove-wishlist')
]