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
        'iat' :  datetime.utcnow()                  #iat is initiation time   
    }    
    access_token = jwt.encode(payload, 'secret', algorithm='HS256')
    
    return access_token

class UserSignup(APIView):
    def post(self, request):
        serializer = serializers.UserSerializer(data=request.data)
        if serializer.is_valid():
            user_name = serializer.validated_data['username']
            if models.User.objects.filter(username=user_name).exists():
                return Response({'error': 'Username already exists'})
                        
            serializer.save(
                password=make_password(serializer.validated_data['password']),
            )
            return Response({'message': 'User signed up successfully'})
                               
        else:
            return Response({'error':serializer.errors})
    
class UserLogin(APIView):
    def post(self, request):
        serializer = serializers.UserSerializer(data=request.data)
        if serializer.is_valid():
            user_name = serializer.validated_data['username']
            pass_word = serializer.validated_data['password']
            try:
                logged_user = models.User.objects.get(username=user_name)
            except Exception as e:
                return Response({'message':'Incorrect username or password'})
            password_check = check_password(pass_word, logged_user.password)
            if password_check :
                token = generate_access_token(logged_user)
                response = Response()
                response.set_cookie('access_token', value=token, httponly=True)
                response.data = {
                    'message' : 'login success',
                    'access_token' : token
                }
                return response
            return Response({'error' : 'Invalid username or password'})
