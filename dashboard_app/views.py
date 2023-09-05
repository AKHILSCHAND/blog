from django.shortcuts import get_object_or_404, render, redirect
from blogapp.models import *
from django.contrib.auth.decorators import login_required
from .forms import categoryform

# Create your views here.
@login_required(login_url='log_in')
def dashboard(request):
    category_count=category.objects.all().count()
    blogs_count=blogs.objects.all().count()
    context = {
        'category_count':category_count,
        'blogs_count':blogs_count
    }
    return render(request, 'dashboard/dashboard.html',context)



def categories(request):
    return render(request, 'dashboard/categories.html')

def add_categories(request):
    if request.method=='POST':
        form = categoryform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('categories')
    form = categoryform()
    context = {
        'form':form,
    }
    return render(request,'dashboard/add_categories.html', context)


def edit_categories(request, pk):
    category_ = get_object_or_404(category, pk=pk)
    if request.method == 'POST':
        form = categoryform(request.POST,instance=category_ )
        if form.is_valid():
            form.save()
            return redirect('categories')
    form = categoryform(instance=category_)
    context = {
        'form':form,
        'category_':category_
    }
    return render( request, 'dashboard/edit_categories.html', context)


def delete_categories(request, pk):
    category_ = get_object_or_404(category, pk=pk)
    category_.delete()
    return redirect('categories')
