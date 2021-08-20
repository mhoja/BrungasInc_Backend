from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Post(models.Model):
    user= models.ForeignKey(User, on_delete=models.PROTECT)
    author= models.CharField(max_length=200, null=True, blank=True)
    post_title = models.CharField(max_length=200, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.post_title}'

class UserRole(models.Model):
    role_name= models.CharField(max_length=200, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    
    def __str__(self):
        return f'{self.role_name}'

class UserProfile(models.Model):
    user= models.ForeignKey(User, on_delete=models.PROTECT)
    user_roleId= models.ForeignKey(UserRole, on_delete=models.PROTECT)
    gender = models.TextField(null=True, blank=True)
    # profile_image = models.ImageField()

    def __str__(self):
        return f'{self.user_roleId}'

class Products(models.Model):
    product_name= models.CharField(max_length=200, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    client_name= models.CharField(max_length=200, null=True, blank=True)
    # product_image = models.ImageField()

    def __str__(self):
        return f'{self.product_name}'

class Testimonial(models.Model):
    customer_name= models.CharField(max_length=200, null=True, blank=True)
    quote = models.TextField(null=True, blank=True)
    # product_image = models.ImageField()

    def __str__(self):
        return f'{self.customer_name}'