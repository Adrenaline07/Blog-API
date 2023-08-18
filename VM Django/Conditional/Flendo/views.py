from django.shortcuts import render
from rest_framework.response import Response 
from rest_framework.views import APIView
from rest_framework import status
from django.http import HttpResponse
from . import serializers
from . import models
#from django.contrib.auth.models import User  # Import User model
from django.contrib.auth.hashers import make_password, check_password
from datetime import datetime, timedelta
import jwt  #the jwt libbrary
from django.db.models import Q

def generate_access_token(user):        
    payload ={
        'user_id' : user.id,
        'exp' : datetime.utcnow() + timedelta(days=5),   
        'iat' :  datetime.utcnow()             
    }    
    access_token = jwt.encode(payload, 'secret', algorithm='HS256')
    
    return access_token
class SellerSignup(APIView):
    def post(self, request):
        serializer = serializers.SellerSerializer(data=request.data)
        if serializer.is_valid():
            user_name = serializer.validated_data['username']
            if models.Seller.objects.filter(username=user_name).exists():
                return Response({'error': 'Username already exists'})
                        
            serializer.save(
                password=make_password(serializer.validated_data['password']),
            )
            return Response({'message': 'User signed up successfully'})
                               
        else:
            return Response({'error':serializer.errors})