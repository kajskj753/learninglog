from django.conf.urls import re_path
from . import views
app_name='MyApp'
urlpatterns = [

    re_path(r'^$',views.index,name = 'index'),
    re_path(r'^topics/(?P<topic_id>\d+)/$',views.topic,name = 'topic'),
    re_path(r'^topics/$',views.topics,name = 'topics'),
]