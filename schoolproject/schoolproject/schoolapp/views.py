from django.contrib import auth,messages
from django.contrib.auth import authenticate
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth.models import User
from django.shortcuts import (render,redirect)

from django import forms

from django.urls import reverse


# Create your views here.
def demo(request):
    return render(request,"home.html")
#

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('/new/')
        else:
            messages.info(request,"invalid credentials")
    return render(request, 'login.html')





def register(request):
    form=UserCreationForm()
    if request.method == 'POST':
        form=UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            print('registered successfully')
            return redirect('/login/')
    return render(request, 'register.html', {'form': form})
    #
    #     form = RegisterForm()



def new(request):

    return render(request,"new.html")
def new_page(request):

    return render(request,"new_page.html", )
def index(request):
    return render(request,"index.html")
def logout(request):
    auth.logout(request)
    return redirect('/')
