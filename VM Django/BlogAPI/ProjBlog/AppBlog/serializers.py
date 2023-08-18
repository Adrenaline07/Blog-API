from rest_framework import serializers
from . import models

class UserSerializer(serializers.ModelSerializer):
    class Meta : 
        model = models.User
        fields = ('id' , 'username', 'password' )
        read_only_fields = ('id',)

class LoginSerializer(serializers.ModelSerializer):
    class Meta : 
        model = models.User
        fields = ('id' , 'username', 'password' )
        read_only_fields = ('id',)

class PostSerializer(serializers.ModelSerializer):
    class Meta : 
        model = models.Post
        fields = ('id', 'posttitle' , 'postcontent',  'postdate', 'postOwner')
        read_only_fields = ('id', )
        
