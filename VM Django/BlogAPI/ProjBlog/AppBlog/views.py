from django.shortcuts import render
from rest_framework.response import Response 
from rest_framework.views import APIView
from rest_framework import status
from django.http import HttpResponse
from . import serializers
from . import models
from django.contrib.auth.hashers import make_password, check_password
from datetime import datetime, timedelta
import jwt  #the jwt libbrary


def generate_access_token(user):        #generate a token for the user, so your frontend or mobile app programmer can use it
    payload ={
        'user_id' : user.id,
        'exp' : datetime.utcnow() + timedelta(days=5),   # timedelta is for extratime/usagetime, utcnow is current time
        'iat' :  datetime.utcnow()             #iat is initiated time
    }    
    #to construct token
    access_token = jwt.encode(payload, 'secret', algorithm='HS256')
    
    return access_token


class Signup(APIView):
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
            return Response({'error': serializer.errors})
                
class Login(APIView):
    def post(self, request):
        serializer = serializers.LoginSerializer(data = request.data)   #every serializer has data
        if serializer.is_valid(): 
            # username = request.data.get('username)
            user_name = serializer.validated_data.get('username')
            pass_word = serializer.validated_data['password']       #sqr bracket works same way as .get()
            try:
                logged_user = models.User.objects.get(username=user_name)
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
        
class Post(APIView):
    def post(self, request):
        token = request.COOKIES.get('access_token')
        if not token:
            return Response({'message' : 'unautheticated'})
        try :
            payload = jwt.decode(token, 'secret', algorithms=['HS256'])
        except Exception as e: 
            return Response({'error': str(e)})
        serializer = serializers.PostSerializer(data = request.data)   #every serializer has data
        try : 
            logged_user = models.User.objects.get(id=payload['user_id'])
        except Exception as e:
            return Response({'error' : str(e)})
        
        if serializer.is_valid(): 
            serializer.save(postOwner=logged_user)
            return Response({'message':' post created successfully', 'post_data': serializer.data})
        return Response({'error': 'data is not valid'})

#TO READ POST
    def get(self, request):
        token = request.COOKIES.get('access_token')
        if not token:
            return Response({'message' : 'unautheticated'})
        try :
            payload = jwt.decode(token, 'secret', algorithms=['HS256'])
        except Exception as e: 
            return Response({'error': str(e)})
        serializer = serializers.PostSerializer(data = request.data)   #every serializer has data
        try : 
            logged_user = models.User.objects.get(id=payload['user_id'])
        except Exception as e:
            return Response({'error' : str(e)})
        
        posts = models.Post.objects.all()
        serializer = serializers.PostSerializer(posts, many=True)
        #      posts_data = [{"title": post.posttitle, "content": post.postcontent} for post in posts]
        return Response({"posts": serializer.data})  
#TO UPDATE POST
    def put(self, request):             #to edit a post
        token = request.COOKIES.get('access_token')
        if not token:
            return Response({'message' : 'unautheticated'})
        try :
            payload = jwt.decode(token, 'secret', algorithms=['HS256'])
        except Exception as e: 
            return Response({'error': str(e)})
        serializer = serializers.PostSerializer(data = request.data)   #every serializer has data
        try : 
            logged_user = models.User.objects.get(id=payload['user_id'])
        except Exception as e:
            return Response({'error' : str(e)})
        
        post_id  = request.query_params.get('post_id')
        try :
            post_to_update = models.Post.objects.get(id=post_id)
            if post_to_update.postOwner != logged_user:
                return Response({"message":"This post does not belong to you"})
        except Exception as e:
            return Response({'error': 'There is no post with such id'})
        serializer = serializers.PostSerializer(post_to_update, data=request.data, partial = True)  #partial =true helps to run the code without former dependencies
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Post has been updated succesfully', 'data' : serializer.data})
        return Response({'message': str(e)})
#TO DELETE POST
    def delete(self, request):
        token = request.COOKIES.get('access_token')
        if not token:
            return Response({'message' : 'unautheticated'})
        try :
            payload = jwt.decode(token, 'secret', algorithms=['HS256'])
        except Exception as e: 
            return Response({'error': str(e)})
        serializer = serializers.PostSerializer(data = request.data)   #every serializer has data
        try : 
            logged_user = models.User.objects.get(id=payload['user_id'])
        except Exception as e:
            return Response({'error' : str(e)})

        #post_id = request.data.get('post_id')   OR    #post_id = request.query_params.get('post_id') is used for direct delete using id
        post_id = request.query_params.get('post_id')
        post_to_delete = models.Post.objects.get(id=post_id)
        try : 
            post_to_delete.delete()
            return Response({'message' : 'post deleted successfully'})
        except Exception as e:
            return Response({'error' : 'Post no longer exist'}) 