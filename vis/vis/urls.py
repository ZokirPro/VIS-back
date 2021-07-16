from django.contrib import admin
from django.urls import path,re_path,include
from . import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('owners/',include('owners.urls'),name='owners'),   
    re_path(r'^.*', views.other_html, name='template'),
    

]
