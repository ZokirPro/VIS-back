from django.contrib import admin
from django.urls import path,re_path,include
from . import views
app_name='owners'
urlpatterns = [
    path('jismoniy-shaxslar',views.jismoniyIndex,name='jismoniy'),
    path('yuridik-shaxslar',views.yuridikIndex,name='yuridik'),
    path('hisobot',views.hisobotIndex,name='hisobot')

]
