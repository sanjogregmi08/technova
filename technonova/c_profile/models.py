from django.db import models

# Create your models here
class Delivery(models.Model):
    id=models.AutoField(auto_created=True,primary_key=True)
    name=models.CharField(max_length=100)
    phone=models.CharField(max_length=100)
    address1 = models.CharField(max_length=100)
    address2 =models.CharField(max_length=100,null=True)
    postcode = models.CharField(max_length=100)
    state=models.CharField(max_length=100)
    area=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    state=models.CharField(max_length=100)
class Meta:
     db_table = "delivery"
