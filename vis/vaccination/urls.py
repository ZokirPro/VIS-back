from django.contrib import admin
from django.urls import path,re_path,include
from . import views
app_name='vaccination'
urlpatterns = [
    path('registration_animals',views.registration_animalsIndex,name='registration_animals'),
    path('spravochnik_kategoriya',views.spravochnik_kategoriyaIndex,name='spravochnik_kategoriya'),
    path('spravichnok_svetov',views.spravichnok_svetovIndex,name='spravichnok_svetov'),
    path('schemes',views.schemesIndex,name='schemes'),
    path('registration_vaccines',views.registration_vaccinesIndex,name='registration_vaccines'),
    path('report_vaccination',views.report_vaccinationIndex,name='report_vaccination')
]   
