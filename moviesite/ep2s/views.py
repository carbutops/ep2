from django.shortcuts import render, get_object_or_404
from .models import Topic, Entry
from .forms import TopicForm, EntryForm
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required





def index(request):
    """Página inicial."""
    return render(request, 'ep2s/index.html')

def topics(request):
    """Exibe todos os tópicos."""
    topics = Topic.objects.order_by('date_posted')
    context = {'topics': topics}
    return render(request, 'ep2s/topics.html', context)

def topic(request, topic_id):
    """Exibe um único tópico e suas entradas."""
    topic = get_object_or_404(Topic, id=topic_id)
    entries = topic.entry_set.order_by('-date_added')
    content_html = None
    if topic.content_file:
        with topic.content_file.open('r') as file:
            content_html = file.read()
    context = {'topic': topic, 'entries': entries, 'content_html': content_html}
    return render(request, 'ep2s/topic.html', context)

def new_topic(request):
    """Adiciona um novo tópico."""
    if request.method != 'POST':
        form = TopicForm()
    else:
        form = TopicForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('topics'))
    context = {'form': form}
    return render(request, 'ep2s/new_topic.html', context)

@login_required
def new_entry(request, topic_id):
    topic = get_object_or_404(Topic, id=topic_id)

    if request.method == 'POST':
        form = EntryForm(request.POST)
        if form.is_valid():
            new_entry = form.save(commit=False)
            new_entry.topic = topic
            new_entry.created_by = request.user  # Associando o usuário logado
            new_entry.save()
            return HttpResponseRedirect(reverse('topic',args= topic_id))  # Redireciona para a página do tópico
    else:
        form = EntryForm()

    return render(request, 'ep2s/new_entry.html', {'form': form, 'topic': topic})


def edit_entry(request, entry_id):
    """Edita uma entrada existente."""
    entry = get_object_or_404(Entry, id=entry_id)
    topic = entry.topic
    if request.method != 'POST':
        form = EntryForm(instance=entry)
    else:
        form = EntryForm(instance=entry, data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('topic', args=[topic.id]))
    context = {'entry': entry, 'topic': topic, 'form': form}
    return render(request, 'ep2s/edit_entry.html', context)
