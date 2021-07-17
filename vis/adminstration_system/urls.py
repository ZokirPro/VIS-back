from django.contrib import admin
from django.urls import path,re_path,include
from . import views
app_name='adminstration_system'
urlpatterns = [
    path('user_adminstration',views.user_adminstrationIndex,name='user_adminstration'),
    path('user_rights',views.user_rightsIndex,name='user_rights'),
    path('audit',views.auditIndex,name='audit'),
    path('archive_restore',views.archive_restoreIndex,name='archive_restore'),
    path('report_adminstration',views.report_adminstrationIndex,name='report_adminstration')
]   
