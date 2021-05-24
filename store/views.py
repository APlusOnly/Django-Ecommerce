from django.shortcuts import render, redirect
from store.models import *

def home(request):
    items = Item.objects.all()
    departments = Department.objects.all()

    context = {
        'items': items, 'departments': departments
    }

    return render(request, '', departments, context)

