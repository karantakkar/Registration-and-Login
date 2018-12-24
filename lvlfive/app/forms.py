from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User
from app.models import UserProfileInfo

class userform(ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta():
        model = User
        fields = ('username','email','password')

class UserProfileInfoForm(ModelForm):  
    class Meta():
        model = UserProfileInfo
        fields = ('portfolio_site','profile_pic')
