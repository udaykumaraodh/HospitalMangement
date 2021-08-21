from django.db import models

# Create your models here.
from django.contrib.auth import get_user_model

# Create your models here.

User=get_user_model()
class Sales(models.Model):
    user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
    name=models.CharField(max_length=50)
    #photo=models.ImageField(upload_to='sales_profile/')
    gender=models.CharField(max_length=20)
    dob=models.DateField()
    mobile=models.BigIntegerField(unique=True)
    emailId=models.EmailField(max_length=150)
    qualificaton=models.CharField(max_length=50)
    address=models.CharField(max_length=200)

    def __str__(self):
        return  self.name

class PreRegHos(models.Model):
    hospital_name=models.CharField(max_length=80,unique=True)
    h_address=models.CharField(max_length=150)
    mobile=models.BigIntegerField(unique=True)
    allocate_to=models.OneToOneField(Sales,on_delete=models.CASCADE)

    def __str__(self):
        return self.hospital_name



