from django.shortcuts import render
from .models import Topic,Entry
# Create your views here.
def index(request):
    return render(request,'MyApp/index.html')


def topics(request,topic_id):
    """显示所有主题"""

    topics = Topic.objects.get(id=topic_id)
    entries = topics.entry_set.order_by('-data_added')
    context = {'topics':topics,'entries':entries}
    return render(request,'MyApp/topic.html',context)