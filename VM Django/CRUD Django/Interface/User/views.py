
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


def generate_access_token(user):        #generate a token for the user, so your frontend or mobile app programmer can use it
    payload ={
        'user_id' : user.id,
        'exp' : datetime.utcnow() + timedelta(days=5),   # timedelta is for extratime/usagetime, utcnow is current time
        'iat' :  datetime.utcnow()             #iat is initiated time
    }    
    #to construct token
    access_token = jwt.encode(payload, 'secret', algorithm='HS256')
    
    return access_token

class Test(APIView):        #This is to get request
    def get(self, request): 
        #return HttpResponse("This is a standard API running.")
        return Response({"message" : "this API works", "date" : "11/08/2023"} )
    
    def get(self, request):
        username = request.data['username']
        return Response({'name': f"welcome {username}"})
    
class Signup(APIView):
    def post(self, request):
        serializer = serializers.UserSerializer(data=request.data)
        if serializer.is_valid():
            user_name = serializer.validated_data['username']
            if models.User.objects.filter(username=user_name).exists():
                return Response({'error': 'Username already exists'})
            
            e_mail = serializer.validated_data['email']
            if models.User.objects.filter(email=e_mail).exists():
                return Response({'error': 'Email already exists'})
            
            serializer.save(
                password=make_password(serializer.validated_data['password']),
                firstname=serializer.validated_data['firstname'],
                lastname=serializer.validated_data['lastname'],
                age=serializer.validated_data['age']
            )
            return Response({'message': 'User signed up successfully'})
                                       
        else:
            return Response({'error': serializer.errors})
                
class Login(APIView):
#A problem that occured is if i run this without creating another serializer for LOGIN, and 
#unclick any detail from User serializer in the formdata in POSTMAN it says ASsertion error: AssertionError at /api/login
#Expected a `Response`, `HttpResponse` or `HttpStreamingResponse` to be returned from the view, but received a `<class 'NoneType'>`
#So i'm gonna create another serializer for post so i can click the needed data in formdata
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
        
        # else: 
            # return Response({"error": serializer.errors})
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
        #     return Response({'message': 'Post created successfully'})
        # else:
        #         return Response({'error': serializer.errors})
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

class PersonalPost(APIView):
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
        
        posts = models.Post.objects.filter(postOwner = logged_user)     #This filter filters all posts and brings the post of the currently logged in user
        posts_to_show = serializers.PostSerializer(posts, many = True)
        return Response({'data' : posts_to_show.data})
        
   