from django.shortcuts import get_object_or_404, render, redirect
from  .models import *
from django.db.models import Q
# Create your views here.

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



def blog(request,slug):
    single_post = get_object_or_404(blogs, slug=slug, status='published')
    context = {
        'single_post':single_post,
    }
    return render(request, 'blogs.html',context)


def search(request):
    keyword = request.GET.get('keyword')
    blog_ = blogs.objects.filter(Q(title__icontains=keyword)|Q(short_description__icontains=keyword)|Q(blog_body__icontains=keyword), status='published')
    context = {
        'blog_':blog_,
        'keyword':keyword
    }
    return render (request, 'search.html',context)