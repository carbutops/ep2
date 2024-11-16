from django.shortcuts import render
from .models import Topic, Entry
from .forms import TopicForm
from django.http import HttpResponseRedirect
from django.urls import reverse
# Create your views here.
def index(request):
    return render(request, 'ep2s/index.html')

def topics(request):
    topics = Topic.objects.order_by('date_added')
    context = {'topics': topics }

    return render(request, 'ep2s/topics.html', context)

def topic(request,topic_id):
    topic = Topic.objects.get( id=topic_id)
    entries= topic.entry_set.order_by('-date_added')
    context={ 'topic': topic, 'entries': entries}
    return render(request, 'ep2s/topic.html', context)

def new_topic(request):
    if request.method!= 'POST':
        form= TopicForm()
    else:
        form= TopicForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('topics'))
    context={'form': form}
    return render( request, 'ep2s/new_topic.html', context)


