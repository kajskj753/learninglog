from django.shortcuts import render,redirect
from django.contrib.auth import logout,authenticate,login
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib import auth
from django.contrib.auth.forms import UserCreationForm
# Create your views here.
# def login(request):
#     return render(request, 'users/login.html')

def register(request):
    #注册新用户
    if request.method !='POST':
        #显示空的注册表单
        form = UserCreationForm()

    else:
        #处理填写好的表单
        form = UserCreationForm(data=request.POST)

        if form.is_valid():
            new_user = form.save()
            #用户自动登陆，重定向到主页
            authenticated_user = authenticate(username = new_user.username,password = request.POST['password1'])
            login(request,authenticated_user)
            return HttpResponseRedirect(reverse('MyApp:index'))

    context = {'form':form}
    return render(request, 'users/register.html',context)
#

def logout(request):
    #注销用户,此处与书本略有不同已经修正
    auth.logout(request)

    return HttpResponseRedirect(reverse('MyApp:index'))