from django.contrib import admin
from django.urls import include, path # modificar esta linha

urlpatterns = [
     # adicionar esta linha
    path('admin/', admin.site.urls),
    path('', include('ep2s.urls')),
    path('users/', include('users.urls')),

]