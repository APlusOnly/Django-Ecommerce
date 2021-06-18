from typing import ItemsView
from django.contrib.auth.models import User
from django.http import request
from django.http.response import HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from store.models import *
from django.contrib.auth.decorators import login_required
from django.contrib import messages


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

@login_required
def my_account(request):
    wishlist = Wishlist.objects.all()

    context = {
        'wishlist': wishlist
    }
    return render(request, 'store/my_account.html', context)

def my_cart(request):
    return render(request, 'store/my_cart.html')

def log_in(request):
    return render(request, 'store/log_in.html')

def category_view(request, pk):
    object = get_object_or_404(Category, id=pk)
    categories = Category.objects.order_by('name').filter(department=object.department)
    items = Item.objects.filter(category=object, visible='Visible')
    items_discount = []
    for item in items:
        discount_price = item.retail_price - (item.retail_price * (item.discount_percent/100))
        items_discount.append([item, discount_price])

    context = {
        'object':object,
        'categories':categories,
        'items': items_discount
    }
    
    return render(request, 'store/category_view.html', context)

def item_view(request, pk):
    page_item = get_object_or_404(Item, id=pk)
    discount_price = page_item.retail_price - (page_item.retail_price * (page_item.discount_percent/100))
    wishlist = False
    if request.user.is_authenticated:
        profile = request.user
        if Wishlist.objects.all().filter(user=profile, item=page_item):
            wishlist = True

    context = {
        'object':page_item,
        'discount_price':discount_price,
        'wishlist': wishlist
    }
    return render(request, 'store/item_detail.html', context)

# maybe change with post, weird stuff when you hit back on the browser
def add_wishlist(request, pk):
    if request.user.is_authenticated:
        item = get_object_or_404(Item, id=pk)
        wishlist = Wishlist(item=item, user=request.user)
        wishlist.save()
        messages.success(request, f'{item} add to your wishlist!')
    return redirect(item_view, pk=pk)

def remove_wishlist(request, pk):
    if request.user.is_authenticated:
        page_item = get_object_or_404(Item, id=pk)
        Wishlist.objects.filter(item=page_item).delete()
        messages.success(request, f'{page_item.name} removed from your wishlist!')
    return redirect(item_view, pk=pk)