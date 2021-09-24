from django.shortcuts import render, redirect
from django.http import HttpResponse

from django.contrib import messages, auth
from django.contrib.auth.models import User
from .forms import UserForm


def login(request):
    if request.method != 'POST':
        return render(request, 'accounts/login.html')

    username = request.POST.get('username')
    password = request.POST.get('password')

    user = auth.authenticate(request, username=username, password=password)

    if not user:
        return render(request, 'accounts/login.html')
    
    auth.login(request, user)
    messages.success(request, 'Você fez login com sucesso!')

    return redirect('home')


def register(request):
    if request.method != 'POST':
        form = UserForm()

        return render(request, 'accounts/register.html', {'form': form})

    form = UserForm(request.POST)
    
    if form.is_valid():
        form.save()
        return redirect('home')

    return render(request, 'accounts/register.html', {'form': form})
