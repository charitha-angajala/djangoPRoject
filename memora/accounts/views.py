from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

def register_view(request):

    # 🔐 Prevent logged-in users from registering again
    if request.user.is_authenticated:
        return redirect('home')  # or '/'

    error = None

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        # ❌ Check if user already exists
        if User.objects.filter(username=username).exists():
            error = "Username already exists. Please login."
        else:
            User.objects.create_user(
                username=username,
                password=password
            )
            return redirect('login')

    return render(request, 'accounts/register.html', {'error': error})


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('home')
    return render(request, 'accounts/login.html')


def logout_view(request):
    logout(request)
    return redirect('home')

