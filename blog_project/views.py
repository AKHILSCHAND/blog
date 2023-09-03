# from django.http import HttpResponse
from django.shortcuts import render
from  blogapp.models import *


# def home(request):
#     return HttpResponse('homepage')

def home(request):
    categories = category.objects.all()
    featured_post = blogs.objects.filter(is_featured = True, status= 'published').order_by('-updated_at')
    post = blogs.objects.filter(is_featured=False, status = 'published')
    context = {
        'categories' : categories,  
        'featured_post': featured_post,
        'post': post,
    }
    return render (request, 'home.html', context)

