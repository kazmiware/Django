from django.db import models
from django.contrib.auth.models import User
from django.shortcuts import reverse
from item.models import Item
# Create your models here.


class Cart(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='cart', null=True)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)

    def get_cart_url(self):
        return reverse("cart:order", kwargs={'id': self.id})

    def get_cart_delete_url(self):
        return reverse("cart:delete_item", kwargs={'id': self.id})


class Order(models.Model):

    name = models.CharField(max_length=10)
    email = models.EmailField()
    address = models.CharField(max_length=20)