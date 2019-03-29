from django.shortcuts import render
from .models import Topic,Entry
# Create your views here.
def index(request):
    return render(request,'MyApp/index.html')


def topic(request,topic_id):
    """显示所有主题"""

    topic = Topic.objects.get(id=topic_id)
    entries = topic.entry_set.order_by('-data_added')
    context = {'topics':topic,'entries':entries}
    return render(request,'MyApp/topic.html',context)

def topics(request):
    topics = Topic.objects.order_by('data_added')
    context = {'topics':topics}
    return render(request,'MyApp/topic.html',context)