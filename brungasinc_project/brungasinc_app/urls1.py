# from django.urls import path
# from . import views


# urlpatterns =[

#     path('user/profile/', views.UserProfileViewSet, name='users_profiles'),
#     path('user/role/', views.UserRoleViewSet, name='users_roles'),
#     path('products/', views.ProductsViewSet, name='products'),
#     path('testimonial/', views.TestimonialViewSet, name='testimonial'),
#     path('posts/', views.PostViewSet, name='posts'),
    
#     ]


from rest_framework import routers
from .views import( UserRoleViewSet, UserProfileViewSet,ProductsViewSet,
UserViewSet, PostViewSet, TestimonialViewSet)

router = routers.DefaultRouter()
router = routers.DefaultRouter()

router.register('users',UserViewSet , 'users')
router.register('all_posts',PostViewSet , 'all_posts')
router.register('users/role',UserRoleViewSet , 'user_role')
router.register('user/profile',UserProfileViewSet , 'user_profile')
router.register('testimonial', TestimonialViewSet , 'testimonial')
router.register('products', ProductsViewSet , 'products')

urlpatterns = router.urls  



    