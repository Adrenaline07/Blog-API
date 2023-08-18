
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

class HirerSignup(APIView):
    def post(self, request):
        serializer = serializers.HirerSerializer(data=request.data)
        if serializer.is_valid():
            user_name = serializer.validated_data['username']
            if models.Hirer.objects.filter(username=user_name).exists():
                return Response({'error': 'Username already exists'})
                        
            serializer.save(
                password=make_password(serializer.validated_data['password']),
            )
            return Response({'message': 'User signed up successfully'})
                               
        else:
            return Response({'error':serializer.errors})

class FreelancerSignup(APIView):
    def post(self, request):
        serializer = serializers.FreelancerSerializer(data=request.data)
        if serializer.is_valid():
            user_name = serializer.validated_data['username']
            if models.Freelancer.objects.filter(username=user_name).exists():
                return Response({'error': 'Username already exists'})
            
            serializer.save(
                password=make_password(serializer.validated_data['password']),
                
            )
            return Response({'message': 'User signed up successfully'})
                                       
        else:
            return Response({'error': serializer.errors})

class HirerLogin(APIView):
    def post(self, request):
                
        serializer = serializers.HirerSerializer(data = request.data)   #every serializer has data
        if serializer.is_valid(): 
            # username = request.data.get('username)
            user_name = serializer.validated_data.get('username')
            pass_word = serializer.validated_data['password']       #sqr bracket works same way as .get()
            try:
                logged_user = models.Hirer.objects.get(username=user_name)
            except Exception as e:   #to save the inputs
                return Response({"message" : str(e)},)    #or return Response({"message" : "user is not registered"},)
            #check_password(login_input, db_current_password)
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

class FreelancerLogin(APIView):
    def post(self, request):
                
        serializer = serializers.FreelancerSerializer(data = request.data)   #every serializer has data
        if serializer.is_valid(): 
            # username = request.data.get('username)
            user_name = serializer.validated_data.get('username')
            pass_word = serializer.validated_data['password']       #sqr bracket works same way as .get()
            try:
                logged_user = models.Freelancer.objects.get(username=user_name)
            except Exception as e:   #to save the inputs
                return Response({"message" : str(e)},)    #or return Response({"message" : "user is not registered"},)
            #check_password(login_input, db_current_password)
            password_check = check_password(pass_word, logged_user.password)
            if password_check :
                token = generate_access_token(logged_user)
                response = Response()
                response.set_cookie('free_access_token', value=token, httponly=True)
                response.data = {
                    'message' : 'login success',
                    'free_access_token' : token
                }
                return response
            return Response({'error' : 'Invalid username or password'})
        
class CreateJob(APIView):
    def post(self, request):
        token = request.COOKIES.get('access_token')
        if not token:
            return Response({'message' : 'unautheticated'})
        try :
            payload = jwt.decode(token, 'secret', algorithms=['HS256'])
        except Exception as e: 
            return Response({'error': str(e)})
                      
        try:
            logged_user = models.Hirer.objects.get(id=payload['user_id'])
            if not logged_user:
                return Response({'message': 'Hirer not found or not logged in'})
        except Exception :
            return Response({'error': str(e) }, )
        
        serializer = serializers.JobSerializer(data = request.data)   #every serializer has data
        if serializer.is_valid():
                serializer.save(jobOwner=logged_user)
                return Response({'message': 'Your post has been uploaded successfully', })

class ViewJob(APIView):
    def post(self, request):
        token = request.COOKIES.get('access_token')
        if not token:
            return Response({'message' : 'unautheticated'})
        try :
            payload = jwt.decode(token, 'secret', algorithms=['HS256'])
        except Exception as e: 
            return Response({'error': str(e)})
                
        try:
            logged_user = models.Hirer.objects.get(id=payload['user_id'])
            if not logged_user:
                return Response({'message': 'Freelancer not found or not logged in'})
        except Exception :
            return Response({'error': str(e) }, )
        
        posts = models.Job.objects.all()
        serializer =serializers.JobSerializer(posts, many=True)
        return Response({'message': serializer.data  })
    
class SearchJob(APIView):
    def post(self, request):
        token = request.COOKIES.get('access_token')
        if not token:
            return Response({'message' : 'unautheticated'})
        try :
            payload = jwt.decode(token, 'secret', algorithms=['HS256'])
        except Exception as e: 
            return Response({'error': str(e)})
        try:
            logged_user = models.Job.objects.get(id=payload['user_id'])
        except Exception :
            return Response({'error': str(e) }, )
        
        search_job = request.query_params.get('search')
        posts = models.Job.objects.filter(Q(jobTitle__icontains=search_job))
        if posts:
            posts_to_show = serializers.JobSerializer(posts, many=True)
            return Response({'data': posts_to_show.data})
        return Response({'message':'Nothing found'})