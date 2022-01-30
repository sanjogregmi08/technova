from django.db import models

# Create your models here.
class Products(models.Model):
    
    id=models.AutoField(primary_key=True,auto_created=True)
    name=models.CharField(max_length=200)
    category=models.CharField(max_length=100)
    brand=models.CharField(max_length=100)
    item=models.CharField(max_length=100)
    price=models.CharField(max_length=50)
    image=models.CharField(max_length=200)
    
    @property
    def get_total_price(self):
        return sum([Products.price for Products in self.products.all()])

    class Meta:
        db_table = "cart"
