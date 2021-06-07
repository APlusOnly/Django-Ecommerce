from typing import ItemsView
from django.contrib.auth.models import User
from django.http import request
from django.shortcuts import render, redirect, get_object_or_404
from store.models import *
from django.views.generic import (
    DetailView, 
)

def home(request):
    items = Item.objects.all()
    departments = Department.objects.all().order_by('name')

    # get department category
    list = []
    for dep in departments:
        cat = Category.objects.filter(department=dep).order_by('name').first()
        list.append([dep, cat])

    context = {
        'items': items, 'departments': list
    }
    return render(request, 'store/home.html', context)

def departments(request):
    departments = Department.objects.all()
    list = []

    for dep in departments:
        cat = Category.objects.filter(department=dep).order_by('name').first()
        list.append([dep, cat])

    context = {
        'departments': list
    }
    return render(request, 'store/departments.html', context)

def my_account(request):
    return render(request, 'store/my_account.html')

def my_cart(request):
    return render(request, 'store/my_cart.html')

def log_in(request):
    return render(request, 'store/log_in.html')

class CategoryDetailView(DetailView):
    model = Category
    template_name = 'store/category_view.html' 

    def get_context_data(self, **kwargs):
            cat = get_object_or_404(Category, id=self.kwargs.get('pk'))
            context = super(CategoryDetailView, self).get_context_data(**kwargs)
            context['categories'] = Category.objects.order_by('name').filter(department=cat.department)
            context['items'] = Item.objects.filter(category=cat, visible='Visible')
            return context
def item_view(request, pk):
    page_item = get_object_or_404(Item, id=pk)
    discount_price = page_item.retail_price - (page_item.retail_price * (page_item.discount_percent/100))
    wishlist = False
    if request.user.is_authenticated:
        profile = request.user
        if Wishlist.objects.all().filter(user=profile, item=page_item):
            wishlist = True
        else:
            wishlist = False
    context = {
        'object':page_item,
        'discount_price':discount_price,
        'wishlist': wishlist
    }
    return render(request, 'store/item_detail.html', context)
'''
    def get_context_data(self, **kwargs):
        item = get_object_or_404(Item, id=self.kwargs.get('pk'))
        context = super(ItemDetailView, self).get_context_data(**kwargs)
        context['discount_price'] = item.retail_price - (item.retail_price * (item.discount_percent/100))
        #context['reviews'] = Review.objects.filter(order.item==item)
        # check if on wishlist
        if request.user.is_authenticated:
            profile = get_object_or_404(Profile, user=self.request.user)
            context['wishlist'] = Wishlist.objects.all().filter(user=profile.user)
        return context
        '''