
from django.shortcuts import redirect, render
from .forms import Register_form
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import  auth

def register(request):
    if request.method == 'POST':
        form = Register_form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('register')
    else:
        form = Register_form()
    
    context = {
        'form':form
    }
    return render(request, 'registration/register.html',context)

def log_in(request):
    if request.method == 'POST':
        form = AuthenticationForm(request,request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            user = auth.authenticate(username=username, password=password)
            if user is not None:
                auth.login(request, user)
            return redirect('home')
    form = AuthenticationForm()
    context = {
        'form':form
    }
    return render(request, 'registration/log_in.html',context)


def log_out(request):
    auth.logout(request)
    return redirect('home')

