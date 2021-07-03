from django.shortcuts import render, redirect, get_object_or_404
from store.models import Item, Category
from users.models import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (
    DeleteView,
    CreateView,
    UpdateView
)


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

class PaymentCreateView(LoginRequiredMixin, CreateView):
    model = Payment
    fields = ['card_number', 'expire_date', 'cvv', 'first_name', 'last_name', 'type']
    success_url = '/profile/'
    action = 'Create'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def get_action(self):
        return self.action

class PaymentUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Payment
    fields = ['card_number', 'expire_date', 'cvv', 'first_name', 'last_name', 'type']
    success_url = '/profile/'
    action = 'Update'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def test_func(self):
        payment = self.get_object()
        if self.request.user == payment.user:
            return True
        return False

    def get_action(self):
        return self.action

class AddressCreateView(LoginRequiredMixin, CreateView):
    model = Address
    fields = ['country', 'province', 'city', 'street', 'apartment_number', 'postal_code']
    success_url = '/profile/'
    action = 'Create'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def get_action(self):
        return self.action


class AddressDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Address
    success_url = '/profile/'

    def test_func(self):
        address = self.get_object()
        if self.request.user == address.user:
            return True
        return False

class AddressUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Address
    fields = ['country', 'province', 'city', 'street', 'apartment_number', 'postal_code']
    success_url = '/profile/'
    action = 'Update'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def test_func(self):
        address = self.get_object()
        if self.request.user == address.user:
            return True
        return False

    def get_action(self):
        return self.action
