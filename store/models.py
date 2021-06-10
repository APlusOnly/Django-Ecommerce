from django.db import models
from django.contrib.auth.models import User


class Department(models.Model):
    name = models.CharField(max_length=255)
    picture = models.ImageField(default='###image.url')

    def __str__(self):
        return self.name

class Category(models.Model):
    department = models.ForeignKey(Department, null=True ,on_delete=models.SET_NULL)
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
    
'''
class Size(models.Model):
    item = models.ForeignKey(Item, default=)
    size # make a list of choices from xs to xxl
    stock = models.IntegerField() 
'''

class Item(models.Model):
    VISIBLE = (
        ('Visible', 'Visible'),
        ('Not Visible', 'Not Visible')
    )
    STOCK = (
        ('In Stock', 'In Stock'),
        ('Currently Unavailable', 'Currently Unavailable')
    )
  
    SIZE = (
        ('No Size', 'No Size'),
        ('Small', 'Small'),
        ('Medium', 'Medium'),
        ('Large', 'Large'),
        ('X-Large', 'X-Large')
    )
    
    name = models.CharField(max_length=255, null=True)
    cost = models.FloatField(max_length=20, null=True)
    retail_price = models.FloatField(max_length=20, null=True)
    discount_percent = models.FloatField(max_length=3, null=True)
    stock = models.CharField(max_length=255, choices=STOCK, null=True) # might be easier to put stock in size class
    category = models.ForeignKey(Category, null=True ,on_delete=models.SET_NULL)
    visible = models.CharField(max_length=255, choices=VISIBLE, null=True)
    picture = models.ImageField(default= 'default.PNG', null=True, blank=True, upload_to='item_pics')
    brand = models.CharField(max_length=255, null=True)
    size = models.CharField(max_length=255, null=True, choices=SIZE) # make size a foreign key maybe
    description = models.CharField(max_length=255, null=True)

    def __str__(self):
        return self.name


class Profile(models.Model):
    first_name = models.CharField(max_length=255, null=True)
    last_name = models.CharField(max_length=255, null=True)
    email = models.CharField(max_length=255, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        full_name = self.first_name + ' ' + self.last_name
        return full_name


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


# can use the default django User class for some info like name and email, can be user profile
# maybe we can put all the user stuff into a different app, might be a better practice 
class UserProfile(models.Model):
    user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    picture = models.ImageField(default='#imageurl', null=True, blank=True)
    #address = models.ManyToOneRel(Address, on_delete=models.SET_NULL)

# maybe add payment type like credit card information or such if we want
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
        return self.card_number


# maybe add payment to order, so we know how the customer payed for their order
class Order(models.Model): 
    STATUS = (
        ('Pending', 'Pending'),
        ('Out For Delivery', 'Out For Delivery'),
        ('Delivered', 'Delivered')
    )
    item = models.ForeignKey(Item, null=True, on_delete=models.SET_NULL)
    user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    num_items = models.FloatField(max_length=100, null=True)
    address = models.ForeignKey(Address, null=True, on_delete=models.SET_NULL)
    date = models.DateTimeField(auto_now_add=True, null=True)
    status = models.CharField(max_length=200, null=True, choices=STATUS)
    payment_used = models.ForeignKey(Payment, null=True ,on_delete=models.SET_NULL)

    def __str__(self):
        order_details = self.item.name + ' ' + self.date
        return order_details


class Wishlist(models.Model):
    user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    item = models.ForeignKey(Item, null=True, on_delete=models.SET_NULL)

class Review(models.Model):
    RATING = (
        ('1.0', '1.0'),
        ('2.0', '2.0'),
        ('3.0', '3.0'),
        ('4.0', '4.0'),
        ('5.0', '5.0')
    )
    user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    order = models.ForeignKey(Order, null=True, on_delete=models.SET_NULL) # maybe change to item
    description = models.CharField(max_length=255, null=True)
    rating = models.CharField(max_length=255, choices=RATING, null=True)

    def __str__(self):
        return self.rating
