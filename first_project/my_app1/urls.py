from django.urls import path
from my_app1 import views


app_name ='my_app1'

urlpatterns = [
    path('', views.users, name="users"),
    path('', views.help, name="help"),
    path('', views.signup, name="signup"),
    path('', views.register, name="register"),
    path('', views.user_login, name='user_login')

]