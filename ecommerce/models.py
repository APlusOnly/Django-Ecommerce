from django.db import models
from django.contrib.auth.models import User

class Item(models.Model):
    VISIBLE = (
        ('Visible', 'Visible'),
        ('Not Visible', 'Not Visible')
    )
    STOCK = (
        ('In Stock', 'In Stock'),
        ('Currently Unavailable', 'Currently Unavailable')
    )
    DEPARTMENT = (
        ('Automotive', (
            ('Automotive Care', 'Automotive Care'),
            ('Car Electronics & Accessories', 'Car Electronics & Accessories'),
            ('Lights & Lighting Accessories', 'Lights & Lighting Accessories'),
            ('Tires & Wheels', 'Tires & Wheels'),
            ('Tools & Equipment', 'Tools & Equipment'))
         ),
        ('Books', (
            ('Arts & Photography', 'Arts & Photography'),
            ('Business & Investing', 'Business & Investing'),
            ('Comics & Graphic Novels', 'Comics & Graphic Novels'),
            ('Computers & Technology', 'Computers & Technology'),
            ('History', 'History'),
            ('Literature & Fiction', 'Literature & Fiction'),
            ('Romance', 'Romance'),
            ('Science & Math', 'Science & Math'),
            ('Travel', 'Travel'))
         ),
        ('Clothing, Shoes & Accessories', (
            ('Boys', 'Boys'),
            ('Girls', 'Girls'),
            ('Women', 'Women'),
            ('Men', 'Men'))
         ),
        ('Electronics', (
            ('Accessories & Supplies', 'Accessories & Supplies'),
            ('Camera, Photo & Video', 'Camera, Photo & Video'),
            ('Cell Phones & Accessories', 'Cell Phones & Accessories'),
            ('Computers & Accessories', 'Computers & Accessories'),
            ('Home Audio', 'Home Audio'),
            ('Office Electronics', 'Office Electronics'),
            ('Televisions & Video', 'Televisions & Video'))
         ),
        ('Home & Kitchen', (
            ('Arts, Crafts & Sewing', 'Arts, Crafts & Sewing'),
            ('Bath', 'Bath'),
            ('Furniture', 'Furniture'),
            ('Home Textiles', 'Home Textiles'),
            ('Storage & Organization', 'Storage & Organization')
        )),
        ('Sports & Outdoors', (
            ('Athletics', 'Athletics'),
            ('Baseball', 'Baseball'),
            ('Basketball', 'Basketball'),
            ('Football', 'Football'),
            ('Hockey', 'Hockey'),
            ('Soccer', 'Soccer'),
            ('Tennis', 'Tennis'),
            ('Volleyball', 'Volleyball'))
         ),
        ('Toys & Games', (
            ('Action & Toy Figures', 'Action & Toy Figures'),
            ('Bikes, Scooters & Ride-Ons', 'Bikes, Scooters & Ride-Ons'),
            ('Games & Accessories', 'Games & Accessories'),
            ('Puzzles', 'Puzzles')
        ))
    )
    SIZE = (
        ('Small', 'Small'),
        ('Medium', 'Medium'),
        ('Large', 'Large'),
        ('X-Large', 'X-Large')
    )
    name = models.CharField(max_length=255, null=True)
    cost = models.FloatField(max_length=20, null=True)
    retail_price = models.FloatField(max_length=20, null=True)
    discount_percent = models.FloatField(max_length=3, null=True)
    stock = models.CharField(max_length=255, choices=STOCK, null=True)
    department = models.CharField(max_length=255, choices=DEPARTMENT, null=True)
    visible = models.CharField(max_length=255, choices=VISIBLE, null=True)
    picture = models.ImageField(default= '#imageurl', null=True, blank=True)
    brand = models.CharField(max_length=255, null=True)
    size = models.CharField(max_length=255, null=True, choices=SIZE)
    description = models.CharField(max_length=255, null=True)


class Address(models.Model):
    user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    country = models.CharField(max_length=255, null=True)
    province = models.CharField(max_length=255, null=True)
    city = models.CharField(max_length=255, null=True)
    street = models.CharField(max_length=255, null=True)
    apartment_number = models.FloatField(max_length=10, null=True)
    postal_code = models.CharField(max_length=10, null=True)


class User(models.Model):
    first_name = models.CharField(max_length=255, null=True)
    last_name = models.CharField(max_length=255, null=True)
    email = models.CharField(max_length=255, null=True)
    picture = models.ImageField(default='#imageurl', null=True, blank=True)
    address = models.ManyToOneRel(Address)

class Payment(models.Model):
    user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    payment_amt = models.FloatField(max_length=20, null=True)

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

class Invoice(models.Model):
    user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    order = models.ForeignKey(Order, null=True, on_delete=models.SET_NULL)
    amount = models.FloatField(max_length=100, null=True)

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
    order = models.ForeignKey(Order, null=True, on_delete=models.SET_NULL)
    description = models.CharField(max_length=255, null=True)
    rating = models.CharField(max_length=255, choices=RATING, null=True)
