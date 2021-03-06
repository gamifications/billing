
from django.db import models

# Create your models here.
class Buyer(models.Model):
    # Details of buyer
    name= models.CharField(max_length=100)
    father_name= models.CharField(max_length=100)
    mobile1= models.CharField(max_length=100)
    mobile2= models.CharField(max_length=100, blank=True)
    address= models.CharField(max_length=100)
    email= models.EmailField(blank=True)
    state= models.CharField(max_length=100)
    district= models.CharField(max_length=100)
    reference_name= models.CharField(max_length=100)
    aadhar_number= models.CharField(max_length=100)
    date_of_entered = models.DateTimeField(auto_now_add=True)
    photo=models.ImageField()
    email_notifications = models.BooleanField(default=False)
    sms_notifications = models.BooleanField(default=False)
    def __str__(self) -> str:
        return self.name

class BuyerEntry(models.Model):
    billnumber= models.BigIntegerField()
    buyer=models.ForeignKey('Buyer', on_delete=models.CASCADE)
    payment_mode= models.CharField(max_length=100)
    date_of_entered = models.DateTimeField(auto_now_add=True)
    date_of_purchase = models.DateField(null=True)

class BuyerEntryItems(models.Model):
    buyer_entry = models.ForeignKey('BuyerEntry', on_delete=models.CASCADE)
    labour_commn= models.IntegerField()
    product = models.ForeignKey('dashboard.Product', on_delete=models.CASCADE)
    unit_type= models.CharField(max_length=100)
    unit_price= models.IntegerField()
    hamali= models.IntegerField()

class Accounting(models.Model):
    buyer=models.ForeignKey('Buyer', on_delete=models.CASCADE)
    is_credit = models.BooleanField(default=False)
    date_of_entered = models.DateTimeField(auto_now_add=True)
    # balance = models.IntegerField()
    amount = models.IntegerField()

