
# urlpatterns =[

#     path('user/profile/', views.UserProfileViewSet, name='users_profiles'),
#     path('user/role/', views.UserRoleViewSet, name='users_roles'),
#     path('products/', views.ProductsViewSet, name='products'),
#     path('testimonial/', views.TestimonialViewSet, name='testimonial'),
#     path('posts/', views.PostViewSet, name='posts'),
    
#     ]


from rest_framework import routers
from .views import( UserRoleViewSet, UserProfileViewSet,ProductsViewSet,
UserViewSet, PostViewSet, TestimonialViewSet,CreateUserView)

router = routers.DefaultRouter()
router = routers.DefaultRouter()

router.register('users',UserViewSet , 'users')
router.register('register', CreateUserView, 'register')
router.register('all_posts',PostViewSet , 'all_posts')
router.register('users_role',UserRoleViewSet , 'user_role')
router.register('user_profile',UserProfileViewSet , 'user_profile')
router.register('testimonial', TestimonialViewSet , 'testimonial')
router.register('products', ProductsViewSet , 'products')

urlpatterns = router.urls  



    