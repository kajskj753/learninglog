from django.shortcuts import render
from .models import Topic,Entry
from django.http import HttpResponseRedirect,HttpResponse
from .forms import TopicForm,EnteyForm
from django.urls import reverse
# Create your views here.
def index(request):
    return render(request,'MyApp/index.html')


def topic(request,topic_id):
    """显示所有主题"""

    topic = Topic.objects.get(id=topic_id)
    entries = topic.entry_set.order_by('-data_added')
    context = {'topic':topic,'entries':entries}
    return render(request,'MyApp/topic.html',context)

def topics(request):
    topics = Topic.objects.order_by('data_added')
    context = {'topics':topics}
    return render(request,'MyApp/topics.html',context)

def new_topic(request):
    """添加新主题"""
    if request.method !='POST':
        #未提交数据,创建一个新表单
        form = TopicForm()
    else:
        #POST提交的数据,对数据进行处理
        form = TopicForm(request.POST)
        #判断数据是否有效
        if form.is_valid():
            # text = form.cleaned_data['text']

            form.save()
            # save_it = form.save(commit=False)
            return HttpResponseRedirect(reverse('MyApp:topics'))

    context = {'form':form}

    return render(request,'MyApp/new_topic.html',context)

def new_entry(request,topic_id):
    """在特定的主题中添加新的条目"""
    topic = Topic.objects.get(id =topic_id)

    if request.method!='POST':
        #未提交数据，创建一个空表单
        form = EnteyForm()
    else:
        #POST提交的数据，对数据进行处理
        form = EnteyForm(data=request.POST)
        if form.is_valid():
            new_entry = form.save(commit=False)
            new_entry.topic = topic
            new_entry.save()
            return HttpResponseRedirect(reverse('MyApp:topic',args = (topic_id)))

    context = {'topic':topic,'form':form}
    # return render(request,'MyApp/new_entry.html',context)
    return render(request, 'MyApp/new_entry.html', context)







