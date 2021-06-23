from django.db import models
from django.contrib.auth.models import User
from store.models import Item

# can see if we can move address and payment here, since it is user stuff

class UserProfile(models.Model):
    user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    picture = models.ImageField(default='#imageurl', null=True, blank=True)
    #address = models.ManyToOneRel(Address, on_delete=models.SET_NULL)

# idk if this needs to be here but 
class Wishlist(models.Model):
    user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    item = models.ForeignKey(Item, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.item.name
