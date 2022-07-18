from django.shortcuts import render
import random
# Create your views here.
def home(request):
    return render(request, 'generator/home.html')

def password(request):

    characters = list('qwertyuiopasdfghjklzxcvbnm')

    length = 10

    thepassword = ''

    for x in range(length):
        thepassword += random.choice(characters)

    uppercase = list('QWERTYUIOPASDFGHJKLZXCVBNM')

    numbers = list('1234567890')

    characters = list('~!@#$%^&*()_+{}:"<>?-+')

    return render(request, 'generator/password.html', {'password':thepassword})
