from django import forms
from blogapp.models import *


class categoryform(forms.ModelForm):
    class Meta:
        model = category
        fields = '__all__'
        
        
class postsform(forms.ModelForm):
    class Meta:
        model = blogs
        fields = ('title','category','featured_image','short_description','blog_body','status','is_featured')
        
        