from django.contrib import admin
from django.urls import path,re_path,include
from . import views
app_name='owners'
urlpatterns = [
    path('fiz',views.fizIndex,name='fiz'),
    path('yurid',views.yuridIndex,name='yurid')
    path('otchot',views.yuridIndex,name='yurid')

]
