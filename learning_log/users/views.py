from django.shortcuts import render,redirect
from django.contrib.auth import logout
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib import auth
# Create your views here.
# def login(request):
#     return render(request, 'users/login.html')

# def register(request):
#     return render(request, 'users/register.html')
#
def logout(request):
    #注销用户,此处与书本略有不同已经修正
    auth.logout(request)

    return HttpResponseRedirect(reverse('MyApp:index'))