from django.shortcuts import render, redirect
from django.http import HttpResponse

from django.contrib.auth.models import User
from .forms import UserForm


def registration(request):
    if request.method != 'POST':
        form = UserForm()

        return render(request, 'accounts/register.html', {'form': form})

    form = UserForm(request.POST)
    
    if form.is_valid():
        form.save()
        return redirect('home')

    return render(request, 'accounts/register.html', {'form': form})
