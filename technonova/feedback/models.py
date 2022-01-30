from django.db import models

class Feedback(models.Model):
    id=models.AutoField(auto_created=True,primary_key=True)
    name=models.CharField( max_length=100)
    phone =models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    type=models.CharField(max_length=100)
    subject=models.CharField(max_length=255)

class Meta:
        db_table ="feedback"

