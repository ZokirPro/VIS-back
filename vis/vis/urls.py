from django.contrib import admin
from django.urls import path,re_path,include
from . import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('owners/',include('owners.urls'),name='owners'),   
    path('vaccines/',include('vaccines.urls'),name='vaccines'),
    path('vaccination/',include('vaccination.urls'),name='vaccination'),
]
