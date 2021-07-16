from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def settings_supportIndex(request):
    context={}

    return render(request,'interactions/settings_support/index.html',context)

def report_interactionsIndex(request):
    context={}
    return render(request,'interactions/report_interactions/index.html',context)