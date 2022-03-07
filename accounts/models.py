from email.policy import default
from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Account(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    age=models.IntegerField(default="21")
    def __str__(self):
        return self.user.username


class contactdetails(models.Model):
    
    contactid = models.AutoField(primary_key=True)

    firstname = models.CharField(max_length=30)
    lastname = models.CharField(max_length=30)

    country_choices = [('India','India'),('United States',"United States")]
    country = models.CharField(choices=country_choices,default="IN",max_length=20)
    subject = models.CharField(max_length=500)
    def __str__(self):
        return self.firstname