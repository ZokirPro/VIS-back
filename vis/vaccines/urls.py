from django.contrib import admin
from django.urls import path,re_path,include
from . import views
app_name='vaccines'
urlpatterns = [
    path('arrival',views.arrivalIndex,name='arrival'),
    path('handbook',views.handbookIndex,name='handbook'),
    path('distribution',views.distributionIndex,name='distribution'),
    path('consumption_rate',views.consumption_rateIndex,name='consumption_rate'),
    path('report_vaccines',views.reportIndex,name='report_vaccines')
]   
