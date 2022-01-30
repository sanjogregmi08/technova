from django.db import models

# Create your models here.
class Products1(models.Model):
    id=models.AutoField(auto_created=True,primary_key=True)
    name=models.CharField(max_length=200)
    category=models.CharField(max_length=100)
    brand=models.CharField(max_length=100)
    item=models.CharField(max_length=100)
    price=models.CharField(max_length=100)
    image=models.FileField(upload_to='products',default="product.jpg")

    class Meta:
        db_table = "products"
