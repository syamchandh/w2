
from django.db import models

# Create your models here.
class productdetails(models.Model):
    employee_name=models.CharField(max_length=255)
    
    dob=models.DateField()
     
    address=models.TextField(max_length=255)
    mobile=models.IntegerField()
    emaill=models.TextField()
    Gend=models.CharField(max_length=255)
    Quali=models.CharField(max_length=255)