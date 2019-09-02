from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User, auth

def index(request):
    return render(request, 'signUp.html')
# Create your views here.

def register(request):
    if request.method == 'POST':
        email = request.POST['email']
        username = request.POST['username']
        pass2 = request.POST['psw']

        user = User.objects.create_user(username=username, email=email, password=pass2)
        user.save()
        print('user created')
        return render(request, 'loggedIn.html')

def logInPage(request):
    return render(request, 'LogIn.html')

def LoggingIn(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            print("NOT EMPTy")
            auth.login(request,user)
            return render(request,'loggedIn.html')
