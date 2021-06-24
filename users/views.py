from django.shortcuts import render, redirect, get_object_or_404
from store.models import Item, Category
from users.models import *
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def my_account(request):
    wishlist = Wishlist.objects.filter(user=request.user)

    context = {
        'wishlist': wishlist
    }
    return render(request, 'users/my_account.html', context)