from django.db import models

# Create your models here.

#Create models for Userdetails

class UserDB(models.Model):
    name=models.CharField(max_length=100,null=True,blank=True)
    email=models.EmailField(max_length=100,null=True,blank=True)
    mobile=models.IntegerField(null=True,blank=True)

class ProductDB(models.Model):
    name=models.CharField(max_length=100,null=True,blank=True)
    price=models.IntegerField(null=True,blank=True)

