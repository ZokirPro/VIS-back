from django.contrib import admin
from django.urls import path,re_path,include
from . import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('owners/',include('owners.urls'),name='owners'),   
    path('vaccines/',include('vaccines.urls'),name='vaccines'),
    path('vaccination/',include('vaccination.urls'),name='vaccination'),
    path('diagnostics/',include('diagnostics.urls'),name='diagnostics'),
    path('interactions/',include('interactions.urls'),name='interactions'),
    path('monitoring/',include('monitoring.urls'),name='monitoring'),
    path('information_services/',include('information_services.urls'),name='information_services'),
    path('adminstration_system/',include('adminstration_system.urls'),name='adminstration_system'),
    path('security/',include('security.urls'),name='security'),
]
