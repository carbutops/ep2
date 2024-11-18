from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Topic(models.Model):
    """Representa um tópico com título, arquivo HTML e data de postagem."""
    text = models.CharField(max_length=250)
    content_file = models.FileField(upload_to='topics/')
    date_posted = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """Representação do modelo."""
        return self.text

class Entry(models.Model):
    """Representa uma entrada vinculada a um tópico."""
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    text = models.CharField(max_length=250)
    date_added = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = 'entries'

    def __str__(self):
        """Representação do modelo."""
        return self.text[:50] + '...'


