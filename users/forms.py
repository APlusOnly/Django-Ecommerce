from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.forms.fields import DateTimeField
from .models import Payment
import datetime

# idk how to properly implement forms into class views
class PaymentCreationForm(forms.Form):
    expire_date = forms.DateField(initial=datetime.date.today, widget=forms.DateInput(attrs={'placeholder':'MM/DD'}))