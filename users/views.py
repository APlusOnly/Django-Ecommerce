from django.shortcuts import render, redirect, get_object_or_404
from store.models import Item, Category
from users.models import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .forms import PaymentCreationForm
from django.views.generic import (
    DeleteView,
    CreateView,
    UpdateView,
    FormView,
    ListView
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

class PaymentCreateView(LoginRequiredMixin, FormView, CreateView):
    model = Payment
    #form_class = PaymentCreationForm
    fields = ['card_number', 'first_name', 'last_name', 'expire_date', 'cvv', 'type']
    success_url = '/profile/'
    action = 'Create'
    template_name = "users/payment_form.html"

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

class AddressListView(LoginRequiredMixin, ListView):
    model: Address
    context_object_name = 'addresses'

    def get_queryset(self):
        user1 = self.request.user
        return Address.objects.filter(user=user1)

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
