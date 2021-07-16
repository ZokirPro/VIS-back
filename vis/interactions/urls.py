from django.urls import path
from . import views
app_name='interactions'
urlpatterns = [
    path('settings_support',views.settings_supportIndex,name='settings_support'),
    path('report_interactions',views.report_interactionsIndex,name='report_interactions')
]   
