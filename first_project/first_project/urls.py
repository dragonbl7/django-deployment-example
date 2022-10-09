"""first_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from my_app1 import views


urlpatterns = [
    path('', views.index, name='index'),
    #path('my_app1/', include('my_app1.urls')),
    path('my_app1/', include('my_app1.urls')),
    path('help/', views.help, name="help"),
    path('users/', views.users, name="users"),
    path('admin/', admin.site.urls),
    path('signup/', views.signup, name="signup"),
    path('about/', views.about, name="about"),
    path('base/', views.base, name="base"),
    path('register/', views.register, name="register"),
    path('logout/', views.user_logout, name="logout"),
    path('special/', views.special, name='special'),
    path('user_login/', views.user_login, name='user_login'),


]
