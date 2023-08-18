from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class User(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=25, null=False)
    firstname = models.CharField(max_length=25, null=True)
    lastname = models.CharField(max_length=25, null=True)
    email = models.CharField(max_length=50, null=True)
    age = models.PositiveIntegerField(null=True)
    password = models.CharField(max_length=50, null=False)


class Post(models.Model):
    posttitle = models.CharField(max_length=50, null=False)
    postcontent = models.CharField(max_length=1500, null=False)
    postOwner = models.ForeignKey(User, on_delete=models.CASCADE, null=True)


    #call the get_owner_username() method directly on a Post instance to retrieve the username of the post's owner:
    
 # Replace 'default_username' with the actual username of the default user
