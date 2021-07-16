from django.contrib import admin
from django.urls import path,re_path,include
from . import views
app_name='vaccines'
urlpatterns = [
    path('registration_animals',views.registration_animalsIndex,name='registration_animals'),
    path('handbook',views.handbookIndex,name='handbook'),
    path('distribution',views.distributionIndex,name='distribution'),
    path('consumption_rate',views.consumption_rateIndex,name='consumption_rate'),
    path('report_vaccines',views.reportIndex,name='report_vaccines')
]   
