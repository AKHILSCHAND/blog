from django.shortcuts import render, redirect
from  .models import *

# Create your views here.

def post_by_category(request, category_id):

    posts = blogs.objects.filter(category=category_id, status="published")
    try:
        category_ = category.objects.get(pk=category_id)
    except:
        return redirect ("home")
    

    context = {
        "posts":posts,
        'category_':category_,
    }
    return render(request,'post_by_category.html',context)