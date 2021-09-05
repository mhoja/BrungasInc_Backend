from django.contrib.auth.models import User
from .serializers import UserSerializer
from rest_framework.views import APIView
from rest_framework import status, viewsets,permissions, generics
from rest_framework.permissions import IsAuthenticated, IsAdminUser, AllowAny
from .models import Post, UserProfile, Testimonial, Products,UserRole
from .serializers import (PostSerializer, UserProfileSerializer,UserRoleSerializer
, TestimonialSerializer,ProductsSerializer, UserSerializer)
from django.views.decorators.csrf import csrf_exempt,csrf_protect #Add this

#rregister
from rest_framework.response import Response
from knox.models import AuthToken
from knox.auth import TokenAuthentication

#LOGIN/LOGOUT
# from rest_framework import permissions
from django.contrib.auth import login
from rest_framework.authtoken.serializers import AuthTokenSerializer
from knox.views import LoginView as KnoxLoginView
class LoginView(KnoxLoginView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request, format=None):
        serializer = AuthTokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        login(request, user)
        return super(LoginView, self).post(request, format=None)

# class UserAPI(generics.RetrieveAPIView):
#     permission_classes = [
#         permissions.IsAuthenticated,
#     ]
#     serializer_class = UserSerializer

#     def get_object(self):
#         return self.request.user


#create user
from django.contrib.auth import get_user_model
from rest_framework import mixins, viewsets
from rest_framework.permissions import AllowAny, IsAuthenticated
class CreateUserView(mixins.CreateModelMixin, viewsets.GenericViewSet):
    permission_classes = [AllowAny]
    queryset = get_user_model().objects.all() #This should be added
    serializer_class = UserSerializer

class UserViewSet(viewsets.ModelViewSet):
  
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class UserProfileViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    permission_classes = [
        permissions.IsAuthenticated,
    ]
    serializer_class = UserProfileSerializer   

class UserRoleViewSet(viewsets.ModelViewSet):
    queryset = UserRole.objects.all()
    serializer_class = UserRoleSerializer 

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    permission_classes = [
        permissions.IsAuthenticated,
    ]
    serializer_class = PostSerializer  

class ProductsViewSet(viewsets.ModelViewSet):
    queryset = Products.objects.all()
    permission_classes=[
        permissions.IsAuthenticated,
    ]
    serializer_class = ProductsSerializer   


class TestimonialViewSet(viewsets.ModelViewSet):
    queryset = Testimonial.objects.all()
    permission_classes=[
        permissions.IsAuthenticated,
    ]
    serializer_class = TestimonialSerializer  