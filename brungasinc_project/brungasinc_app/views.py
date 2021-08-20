from django.contrib.auth.models import User
from .serializers import UserSerializer
from rest_framework.views import APIView
from rest_framework import status, viewsets,permissions, generics
from rest_framework.permissions import IsAuthenticated, IsAdminUser, AllowAny
from .models import Post, UserProfile, Testimonial, Products,UserRole
from .serializers import PostSerializer, UserProfileSerializer,UserRoleSerializer, TestimonialSerializer,ProductsSerializer




class UserViewSet(viewsets.ModelViewSet):
  
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class UserProfileViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    # permission_classes = [
    #     permissions.IsAuthenticated,
    # ]
    serializer_class = UserProfileSerializer   

class UserRoleViewSet(viewsets.ModelViewSet):
    queryset = UserRole.objects.all()
    serializer_class = UserRoleSerializer 

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer  

class ProductsViewSet(viewsets.ModelViewSet):
    queryset = Products.objects.all()
    serializer_class = ProductsSerializer   

class TestimonialViewSet(viewsets.ModelViewSet):
    queryset = Testimonial.objects.all()
    serializer_class = TestimonialSerializer  