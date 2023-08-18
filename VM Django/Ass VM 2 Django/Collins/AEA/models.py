from django.db import models

class Hirer(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=255, null=False)
    password = models.CharField(max_length=100, null=False)
   
class Freelancer(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=255, null=False)
    password = models.CharField(max_length=100, null=False)    

class Job(models.Model):
    id = models.AutoField(primary_key=True)
    jobdescription = models.CharField(max_length=255, null=False)
    jobTitle = models.CharField(max_length=255, null=False)
    jobOwner = models.ForeignKey(Hirer, on_delete=models.CASCADE, null=True)

 

    

