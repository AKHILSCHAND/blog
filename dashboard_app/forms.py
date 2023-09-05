from django import forms
from blogapp.models import *


class categoryform(forms.ModelForm):
    class Meta:
        model = category
        fields = '__all__'