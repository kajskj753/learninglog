from django.shortcuts import render
from .models import Topic,Entry
# Create your views here.
def index(request):
    return render(request,'MyApp/index.html')


def topics(request,topic_id):
    """显示所有主题"""

    topics = Topic.objects.get(id=topic_id)
    context = {'topics':topics}
    return render(request,'MyApp/topic.html',context)