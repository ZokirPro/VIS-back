from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def monitoringIndex(request):
    context={}

    return render(request,'monitoring/index.html',context)