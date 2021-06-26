from django.contrib import admin
from .models import *

admin.site.register(UserProfile)
admin.site.register(Wishlist)
admin.site.register(Address)
admin.site.register(Payment)
