from django.urls import path
from . import views
app_name='information_services'
urlpatterns = [
    path('internal_directories',views.internal_directoriesIndex,name='internal_directories'),
    path('external_directories',views.external_directoriesIndex,name='external_directories'),
    path('report_services',views.report_servicesIndex,name='report_services')

]
