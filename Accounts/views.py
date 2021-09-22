from django.shortcuts import render
from django.http import HttpResponse

from .forms import UserForm


def registration(request):
    form = UserForm()
    return render(request, 'registration/register.html', {'form': form})
