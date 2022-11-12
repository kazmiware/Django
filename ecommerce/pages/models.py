from django.db import models

# Create your models here.


class Contact_form(models.Model):

    name = models.CharField(max_length=10)
    email = models.EmailField(max_length=20)
    subject = models.CharField(max_length=15)
    message = models.TextField(max_length=150)
