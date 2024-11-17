from django.db import models


# Create your models here.

class Topic(models.Model):
    'Um assunto ai'
    text = models.CharField(max_length=250)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        '''representação do modelo'''
        return self.text

class Entry( models.Model ) :
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural= 'entries'

    def __str__(self):
        '''representação do modelo'''
        return self.text[:50] + '...'
