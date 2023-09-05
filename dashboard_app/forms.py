from django import forms
from blogapp.models import *
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class categoryform(forms.ModelForm):
    class Meta:
        model = category
        fields = '__all__'
        
        
class postsform(forms.ModelForm):
    class Meta:
        model = blogs
        fields = ('title','category','featured_image','short_description','blog_body','status','is_featured')
        
class userform(UserCreationForm):
    class Meta:
        model = User
        fields = ('username','email','first_name','last_name','is_active','is_staff','is_superuser','groups','user_permissions')  
        
        
class edituserform(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username','email','first_name','last_name','is_active','is_staff','is_superuser','groups','user_permissions')