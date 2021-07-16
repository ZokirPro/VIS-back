from django.contrib import admin
from django.urls import path,re_path,include
from . import views
app_name='owners'
urlpatterns = [
    path('physical_person',views.physical_personIndex,name='physical_person'),
    path('juridic_person',views.juridic_personIndex,name='juridic_person'),
    path('report_owners',views.reportIndex,name='report_owners')

]
