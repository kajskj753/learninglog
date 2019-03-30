from django.conf.urls import re_path
from . import views
app_name='MyApp'
urlpatterns = [

    re_path(r'^$',views.index,name = 'index'),
    re_path(r'^topics/(?P<topic_id>\d+)/$',views.topic,name = 'topic'),
    re_path(r'^topics/$',views.topics,name = 'topics'),
    #用于添加新主题的网页
    re_path(r'^new_topic/$',views.new_topic,name = 'new_topic'),
    #用于添加新条目的页面
    re_path(r'new_entry/(?P<topic_id>\d+)/$',views.new_entry,name = 'new_entry'),
]