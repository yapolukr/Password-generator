from django.shortcuts import render, redirect
import random
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError
# Create your views here.
def home(request):
    return render(request, 'generator/home.html')

def password(request):

    characters = list('qwertyuiopasdfghjklzxcvbnm')

    if request.GET.get('uppercase'):
        characters.extend(list("QWERTYUIOPASDFGHJKLZXCVBNM"))

    if request.GET.get('numbers'):
        characters.extend(list('1234567890'))

    if request.GET.get('special'):
        characters.extend(list('!@#$%^&*()_+*<>?'))


    length = int(request.GET.get('length'))

    thepassword = ''

    for x in range(length):
        thepassword += random.choice(characters)

    return render(request, 'generator/password.html', {'password':thepassword})

def about(request):
    return render(request, 'generator/about.html')

def copy(request):
    global thepassword
    return (request, thepassword)

def home(request):
    return render(request, 'generator/home.html')

def sign_up(request):
    if request.method == 'GET':
        return render(request, 'generator/sign_up.html', {'form':UserCreationForm()})
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(request.POST['username'], password= request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('currentpasswords')
            except IntegrityError:
                return render(request, 'generator/sign_up.html', {'form': UserCreationForm(), 'error':'This name already exists'})

        else:
            return render(request, 'generator/sign_up.html', {'form': UserCreationForm(), 'error':'The passwords did not match'})

def currenttodos(request):
    return render(request, 'generator/currentpasswords.html')

def logoutuser(request):
    if request.method == 'POST':
        logout(request)
        return redirect('home')

def loginuser(request):
    if request.method == 'GET':
        return render(request, 'generator/login.html', {'form': AuthenticationForm()})
    else:
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'generator/login.html', {'form': AuthenticationForm(), 'error':'Username or password did not match'})
        else:
            login (request, user)
            return redirect('currentpasswords')