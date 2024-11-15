from django.urls import include, path # modificar esta linha
from . import views


urlpatterns = [
     # adicionar esta linha
    path('', views.index, name= 'index'),
    path('topics', views.topics, name= 'topics'),
    path('topics/<topic_id>/', views.topic, name= 'topic'),
]