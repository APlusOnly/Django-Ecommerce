from django.db import models
from django.contrib.auth.models import User


# can see if we can move address and payment here, since it is user stuff

class UserProfile(models.Model):
    user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    picture = models.ImageField(default= 'default.PNG', null=True, blank=True, upload_to='images')
    
    def __str__(self):
        return f'{self.user.username} Profile'

# idk if this needs to be here but 
class Wishlist(models.Model):
    user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    item = models.ForeignKey("store.Item", null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.item.name

class Payment(models.Model):
    TYPES = (
        ('Visa', 'Visa'),
        ('Debit', 'Debit'),
        ('MasterCard', 'Master Card'),
        ('AmericanExpress', 'American Express')
    )
    user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    card_number = models.CharField(max_length=19)
    expire_date = models.DateField()
    cvv = models.CharField(max_length=4)
    type = models.CharField(max_length=100,choices=TYPES)

    def __str__(self):
        return self.card_number[-4:]

class Address(models.Model):
    user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    country = models.CharField(max_length=255, null=True)
    province = models.CharField(max_length=255, null=True)
    city = models.CharField(max_length=255, null=True)
    street = models.CharField(max_length=255, null=True)
    apartment_number = models.FloatField(max_length=10, null=True)
    postal_code = models.CharField(max_length=10, null=True)

    def __str__(self):
        full_address = self.country + ' ' + self.province + ' ' + self.postal_code
        return full_address