from django.shortcuts import render


def signUp(request):
    return render(request, 'baseAccounts.html')
