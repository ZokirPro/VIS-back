from django.contrib import admin
from django.urls import path,re_path,include
from . import views
app_name='diagnostics'
urlpatterns = [
    path('registration_vaccinated_animals',views.registration_vaccinated_animalsIndex,name='registration_vaccinated_animals'),
    path('test_results',views.test_resultsIndex,name='test_results'),
    path('recommendations',views.recommendationsIndex,name='recommendations'),
    path('report_diagnostics',views.report_diagnosticsIndex,name='report_diagnostics')
]   
