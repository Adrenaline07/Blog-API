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
    
class BuyerSignup(APIView):
    def post(self, request):
        serializer = serializers.BuyerSerializer(data=request.data)
        if serializer.is_valid():
            user_name = serializer.validated_data['username']
            if models.Buyer.objects.filter(username=user_name).exists():
                return Response({'error': 'Username already exists'})
            
            serializer.save(
                password=make_password(serializer.validated_data['password']),
                
            )
            return Response({'message': 'User signed up successfully'})
                                       
        else:
            return Response({'error': serializer.errors})

class SellerLogin(APIView):
    def post(self, request):
        serializer = serializers.SellerSerializer(data = request.data)   #every serializer has data
        if serializer.is_valid(): 
            # username = request.data.get('username)
            user_name = serializer.validated_data.get('username')
            pass_word = serializer.validated_data['password']       #sqr bracket works same way as .get()
            try:
                logged_user = models.Seller.objects.get(username=user_name)
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
        
class BuyerLogin(APIView):
    def post(self, request):
        serializer = serializers.BuyerSerializer(data = request.data)   #every serializer has data
        if serializer.is_valid(): 
            # username = request.data.get('username)
            user_name = serializer.validated_data.get('username')
            pass_word = serializer.validated_data['password']       #sqr bracket works same way as .get()
            try:
                logged_user = models.Buyer.objects.get(username=user_name)
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
    
class CreateItem(APIView):
    def post(self, request):
        token = request.COOKIES.get('access_token')
        if not token:
            return Response({'message' : 'unautheticated'})
        try :
            payload = jwt.decode(token, 'secret', algorithms=['HS256'])
        except Exception as e: 
            return Response({'error': str(e)})
                      
        try:
            logged_user = models.Seller.objects.get(id=payload['user_id'])
            if not logged_user:
                return Response({'message': 'Seller not found or not logged in'})
        except Exception :
            return Response({'error': str(e) }, )
        
        serializer = serializers.ItemSerializer(data = request.data)   #every serializer has data
        if serializer.is_valid():
                serializer.save(itemOwner=logged_user)
                return Response({'message': 'Your item has been uploaded successfully', })
        
class ViewItem(APIView):
    def post(self, request):
        token = request.COOKIES.get('access_token')
        if not token:
            return Response({'message' : 'unautheticated'})
        try :
            payload = jwt.decode(token, 'secret', algorithms=['HS256'])
        except Exception as e: 
            return Response({'error': str(e)})
                
        try:
            logged_user = models.Seller.objects.get(id=payload['user_id'])
            if not logged_user:
                return Response({'message': 'Freelancer not found or not logged in'})
        except Exception :
            return Response({'error': str(e) }, )
        
        posts = models.Item.objects.all()
        serializer =serializers.ItemSerializer(posts, many=True)
        return Response({'message': serializer.data  })

class SearchItem(APIView): #What code did we write here to know it's a buyer logging in
    def post(self, request):
        token = request.COOKIES.get('access_token')
        if not token:
            return Response({'message' : 'unautheticated'})
        try :
            payload = jwt.decode(token, 'secret', algorithms=['HS256'])
        except Exception as e: 
            return Response({'error': str(e)})
        try:
            logged_user = models.Item.objects.get(id=payload['user_id'])
        except Exception as e:
            return Response({'error': str(e) } )
        
        search_item = request.query_params.get('search')
        posts = models.Item.objects.filter(Q(itemname__icontains=search_item)| Q(itemdescription__icontains=search_item))   # | is the OR function
        if posts:
            posts_to_show = serializers.ItemSerializer(posts, many=True)
            return Response({'data': posts_to_show.data})
        return Response({'message':'Nothing found'})
    
class UpdateItem(APIView):
    def put(self, request):             #to edit a post
        token = request.COOKIES.get('access_token')
        if not token:
            return Response({'message' : 'unautheticated'})
        try :
            payload = jwt.decode(token, 'secret', algorithms=['HS256'])
        except Exception as e: 
            return Response({'error': str(e)})
        serializer = serializers.ItemSerializer(data = request.data)   #every serializer has data
        try : 
            logged_user = models.Seller.objects.get(id=payload['user_id'])
        except Exception as e:
            return Response({'error' : str(e)})
        
        item_id  = request.query_params.get('item_id')
        try :
            item_to_update = models.Item.objects.get(id=item_id)
            if item_to_update.itemOwner != logged_user:
                return Response({"message":"This item does not belong to you"})
        except Exception as e:
            return Response({'error': 'There is no item with such id'})
        serializer = serializers.ItemSerializer(item_to_update, data=request.data, partial = True)  #partial =true helps to run the code without former dependencies
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'item has been updated succesfully', 'data' : serializer.data})
        return Response({'message': str(e)})