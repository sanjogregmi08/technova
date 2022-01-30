from email.policy import default
from django.db import models

class Customer(models.Model):
    customer_id= models.AutoField(auto_created=True,primary_key=True)
    customer_fullname= models.CharField(max_length=200)
    customer_phonenumber = models.CharField(max_length=10)
    customer_email = models.CharField(max_length=100)
    customer_username = models.CharField(max_length=100)
    cutsomer_password = models.CharField(max_length=100)

class Meta:
    db_table = "customer"

class item(models.Model):
    name=models.CharField(max_length=100)
    price=models.FloatField(max_length=100)
    discount_price = models.FloatField(blank=True ,null=True)
    slug = models.SlugField()
    quantity=models.IntegerField(default=1)

class Meta:
    db_table = "item"
