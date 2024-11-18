from django.urls import path
import views
from django.contrib.auth import views as auth_views

urlpatterns=[
    path('login', auth_views.LoginView.as_view(template_name='user/login.html'),name='login'),
]
