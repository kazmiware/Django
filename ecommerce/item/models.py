from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

# Create your models here.

category_choices = (("S", "Shirt"),
                    ("Sh", "Shoes"),
                    ("W", "Watch"),
                    ("J", "Jewellery")
                    )


class Item(models.Model):

    user = models.ForeignKey(User,
                             on_delete=models.CASCADE,
                             related_name="item",
                             null=True)
    title = models.CharField(max_length=20)
    picture = models.ImageField(default='default.jpg', upload_to='item_pics')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    color = models.CharField(max_length=20)
    category = models.CharField(choices=category_choices, max_length=20)
    description = models.TextField()

    def get_absolute_url(self):

        return reverse("item:item_detail", kwargs={"id": self.id})

    def get_item_url(self):

        return reverse("cart:add_item", kwargs={"id": self.id})

