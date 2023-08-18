from django.db import models

class Seller(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=255, null=False)
    password = models.CharField(max_length=100, null=False)
   
class Buyer(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=255, null=False)
    password = models.CharField(max_length=100, null=False)    

class Item(models.Model):
    id = models.AutoField(primary_key=True)
    itemdescription = models.CharField(max_length=255, null=False)
    itemname = models.CharField(max_length=255, null=False)
    itemOwner = models.ForeignKey(Seller, on_delete=models.CASCADE, null=True)