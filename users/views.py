from django.shortcuts import render, redirect, get_object_or_404
from store.models import Item, Category
from users.models import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (
    DeleteView
)

# Create your views here.
@login_required
def my_account(request):
    wishlist = Wishlist.objects.filter(user=request.user)
    payments = Payment.objects.filter(user=request.user)
    addresses = Address.objects.filter(user=request.user)

    context = {
        'wishlist': wishlist,
        'payments': payments,
        'addresses': addresses
    }
    return render(request, 'users/my_account.html', context)


class PaymentDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Payment
    success_url = '/profile'

    def test_func(self):
        payment = self.get_object()
        if self.request.user == payment.user:
            return True
        return False
