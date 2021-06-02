from django.shortcuts import render, redirect
from store.models import *

def home(request):
    items = Item.objects.all()
    departments = Department.objects.all()

    context = {
        'items': items, 'departments': departments
    }
    return render(request, 'store/home.html', context)

def departments(request):
    departments = Department.objects.all()
    context = {
        'departments': departments
    }
    return render(request, 'store/departments.html', context)

def my_account(request):
    return render(request, 'store/my_account.html')

def my_cart(request):
    return render(request, 'store/my_cart.html')

def log_in(request):
    return render(request, 'store/log_in.html')
