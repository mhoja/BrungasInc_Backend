"""brungasinc_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.urls.conf import re_path
from rest_framework.schemas import get_schema_view
from django.views.generic import TemplateView
from django.conf.urls import url
# from rest_framework_swagger.views import get_swagger_view
from knox import views as knox_views
from django.contrib.auth import views as auth_views
from brungasinc_app.views import LoginView


#SWAGGER
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="BrungasInc API",
        default_version='v1',
        description="Welcome to the Brungas Inc",
        terms_of_service="https://www.jaseci.org",
        contact=openapi.Contact(email="brungasinc@gmail.com"),
        license=openapi.License(name="Awesome BrungasInc API"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    # path("api/login/", auth_views.LoginView.as_view(template_name = "registration/login.html"), name='login'),
    url(r'api/login/', LoginView.as_view(), name='knox_login'),
    url(r'api/logout/', knox_views.LogoutView.as_view(), name='knox_logout'),
    url(r'api/logoutall/', knox_views.LogoutAllView.as_view(), name='knox_logoutall'),
    # url(r'api/register',RegisterAPI , name='register'),
    re_path(r'^doc(?P<format>\.json|\.yaml)$',
            schema_view.without_ui(cache_timeout=0), name='schema-json'),  #<-- Here
    path('BrungasInc/API/V1/doc/', schema_view.with_ui('swagger', cache_timeout=0),
         name='schema-swagger-ui'),  #<-- Here
    path('BrungasInc/API/V1/redoc/', schema_view.with_ui('redoc', cache_timeout=0),
         name='schema-redoc'),  #<-- Here
    path('admin/', admin.site.urls),
    path('api/', include('brungasinc_app.urls1')),
    path('o/', include('oauth2_provider.urls', namespace='oauth2_provider')),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))# FOR SWAGGER
]
