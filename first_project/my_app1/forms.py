from django import forms
from my_app1.models import Signup
from my_app1.models import UserProfileInfo


from django.contrib.auth.models import User


class NewUserForm(forms.ModelForm):
    class Meta:
        model = Signup
        fields = '__all__'


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta():
        model = User
        fields = ('first_name', 'last_name', 'username', 'email', 'password')

class UserProfileInfoForm(forms.ModelForm):

    class Meta():
        model = UserProfileInfo
        fields = ('portfolio_site', 'profile_pic')