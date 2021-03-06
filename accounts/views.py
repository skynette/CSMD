from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from customer.models import Customer

def register(request):
    # if request.user.is_authenticated:
    #     return redirect('/')
    if request.method == "POST":
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password1']
        password2 = request.POST['password2']

        if User.objects.filter(username=username).exists():
            messages.error(request, 'Email already taken')
            return redirect('register')
        elif password != password2:
            messages.error(request, 'Passwords do not match')
            return redirect('register')
        else:
            User.objects.create_user(username=username, password=password, first_name=first_name, last_name=last_name, email=email)
            Customer.objects.create(user=User, name=first_name+" "+last_name)
            messages.success(request, 'Account created')
            return redirect('login')

    context = {

    }
    return render(request, 'accounts/register.html', context)


def login_view(request):
    # if request.user.is_authenticated:
    #     return redirect('/')
    if request.method == "POST":
        username = request.POST['usernmae']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'Successfully logged in')
            messages.success(request, 'Welcome ' + user.first_name)
        else:
            messages.error(request, 'Invalid credentials')
            return redirect('login')
        return redirect('/')
    context = {

    }
    return render(request, 'accounts/login.html', context)


@login_required(login_url="login")
def logout_view(request):
    logout(request)
    messages.success(request, 'You have been logged out')
    return redirect('login')
