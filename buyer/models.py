from unicodedata import name
from django.db import models

# Create your models here.
class Buyer(models.Model):
    # Details of buyer
    name= models.CharField(max_length=100)
    father_name= models.CharField(max_length=100)
    mobile1= models.CharField(max_length=100)
    mobile2= models.CharField(max_length=100)
    address= models.CharField(max_length=100)
    email= models.EmailField(blank=True)
    state= models.CharField(max_length=100)
    district= models.CharField(max_length=100)
    reference_name= models.CharField(max_length=100)
    aadhar_number= models.CharField(max_length=100)
    # date_of_entered
    # photo
    