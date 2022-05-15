"""meshateste URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from recursos.views import home, form, create, view, edit, update, delete
from login.views import login, authentication, register, create_new_user, userlist, delete_user

# API
from django.views.generic.base import TemplateView #Swagger
from rest_framework.schemas import get_schema_view
from rest_framework import routers
from recursos.api import viewsets as recursosviewsets
route = routers.DefaultRouter()
route.register(r'recursos', recursosviewsets.RecursosViewSet, basename='Recursos')

urlpatterns = [
    path('', login, name='login'),
    path('admin/', admin.site.urls),
    path('recursos/', home, name='home'),
    path('recursos/form/', form, name='form'),
    path('recursos/create/', create, name='create'),
    path('recursos/view/<int:pk>/', view, name='view'),
    path('recursos/edit/<int:pk>/', edit, name='edit'),
    path('recursos/update/<int:pk>/', update, name='update'),
    path('recursos/delete/<int:pk>/', delete, name='delete'),
    path('authentication/', authentication, name='authentication'),
    path('login/register/', register, name='register'),
    path('login/createnewuser/', create_new_user, name= 'create_new_user'),
    path('login/userlist/', userlist, name='userlist'),
    path('login/delete/<int:pk>/', delete_user, name='delete_user'),
    path('api/', include(route.urls)),
    #SWAGGER
    path(r'openapi-schema', get_schema_view(
        title='Recursos API',
        description='Recursos API',
        version='1.0.0',
        public=True,
        ), name='openapi-schema'),
    path('docs/', TemplateView.as_view(
        template_name='swagger-ui.html',
        extra_context={'schema_url':'openapi-schema'}
        ), name='swagger-ui')
]