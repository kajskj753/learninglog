from django.conf.urls import re_path
from . import views
from django.contrib.auth.views import login
app_name='users'

urlpatterns = [
    #登陆页面
    re_path(r'^login/$', login,{'template_name':'users/login.html'},name = 'login'),
    # re_path(r'^register/$',views.register,name = 'register'),
    re_path(r'^logout/$',views.logout,name = 'logout'),
]