from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from post.models import Post

# Create your views here.

def home(request):
    posts = Post.objects.all()
    context = {'posts': posts}
    return render(request, 'core/index.html', context)

def signup(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirmpassword = request.POST.get('confirmpassword')
        if password != confirmpassword:
            messages.warning(request, 'Password does not match')
            return redirect('signup')
        elif User.objects.filter(username=username).exists():
            messages.warning(request, 'Username not available')
            return redirect('signup')
        elif User.objects.filter(email=email).exists():
            messages.warning(request, 'Email already registered')
            return redirect('signup')
        else:
            user = User.objects.create_user(username=username, email=email, password=password)
            user.save()
        return redirect('login')
    return render(request, 'registration/signup.html')
   