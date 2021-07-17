from django.contrib import admin
from django.urls import path,re_path,include
from . import views
app_name='security'
urlpatterns = [
    path('security_policy',views.security_policyIndex,name='security_policy'),
    path('access_control',views.access_controlIndex,name='access_control'),
    path('authentication',views.authenticationIndex,name='authentication'),
    path('report_security',views.report_securityIndex,name='report_security')
]   
