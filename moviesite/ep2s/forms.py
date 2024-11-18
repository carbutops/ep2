from django import forms
from .models import Topic, Entry

class TopicForm(forms.ModelForm):
    class Meta:
        model = Topic
        fields = ['text', 'content_file']
        labels = {
            'text': 'Título',
            'content_file': 'Arquivo de conteúdo (HTML)'
        }
        widgets = {
            'text': forms.TextInput(attrs={'placeholder': 'Digite o título do tópico', 'class': 'form-control'}),
            'content_file': forms.ClearableFileInput(attrs={'class': 'form-control'})
        }

class EntryForm(forms.ModelForm):
    class Meta:
        model = Entry
        fields = ['text']
        labels = {'text': 'Texto da entrada'}
        widgets = {
            'text': forms.Textarea(attrs={'cols': 80, 'rows': 5, 'placeholder': 'Digite sua entrada aqui', 'class': 'form-control'})
        }
