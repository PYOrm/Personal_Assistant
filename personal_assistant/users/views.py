from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login
from django.conf import settings
import hashlib


from .forms import RegisterForm, AuthenticationForm

def get_gravatar_url(email, size=100):
    email_hash = hashlib.md5(email.lower().encode('utf-8')).hexdigest()
    return f'https://www.gravatar.com/avatar/{email_hash}?s={size}'

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = True
            user.avatar_url = get_gravatar_url(user.email)
            user.save()
            return redirect('users:login')
    else:
        form = RegisterForm()
    return render(request, 'register.html', {'form': form})

def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            auth_login(request, user)
            return redirect(settings.LOGIN_REDIRECT_URL)
    else:
        form = AuthenticationForm()
    return render(request, 'registration/login.html', {'form': form})

