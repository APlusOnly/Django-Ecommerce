from django.db import models
from django.contrib.auth.models import User
from users.models import Address, Payment

class Department(models.Model):
    name = models.CharField(max_length=255)
    picture = models.ImageField(default='default.jpg', upload_to='images/department')

    def __str__(self):
        return self.name

class Category(models.Model):
    department = models.ForeignKey(Department, null=True ,on_delete=models.SET_NULL)
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Item(models.Model):
    VISIBLE = (
        ('Visible', 'Visible'),
        ('Not Visible', 'Not Visible')
    )
    STOCK = (
        ('In Stock', 'In Stock'),
        ('Currently Unavailable', 'Currently Unavailable')
    )
  

    name = models.CharField(max_length=255, null=True)
    cost = models.FloatField(max_length=20, null=True)
    retail_price = models.FloatField(max_length=20, null=True)
    discount_percent = models.FloatField(max_length=3, null=True)
    category = models.ForeignKey(Category, null=True ,on_delete=models.SET_NULL)
    visible = models.CharField(max_length=255, choices=VISIBLE, null=True)
    picture = models.ImageField(default= 'default.PNG', null=True, blank=True, upload_to='images')
    brand = models.CharField(max_length=255, null=True)
    description = models.CharField(max_length=255, null=True)

    def __str__(self):
        return self.name

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
        return self.item.name + ' ' + self.date
        


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


class Size(models.Model):
    SIZE = (
        ('No Size', 'No Size'),
        ('Small', 'Small'),
        ('Medium', 'Medium'),
        ('Large', 'Large'),
        ('X-Large', 'X-Large')
    )

    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    size = models.CharField(max_length=50)
    stock = models.IntegerField() 