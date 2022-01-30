from django.db import models

class Exchange(models.Model):
    id=models.AutoField(auto_created=True,primary_key=True)
    name=models.CharField(max_length=100)
    c_id=models.CharField(max_length=100)
    type=models.CharField(max_length=100)
    product_id=models.CharField(max_length=100)
    date=models.CharField(max_length=100)
    reason=models.CharField(max_length=200)
    subject=models.CharField(max_length=100)
class Meta:
    db_table ="exchange"
