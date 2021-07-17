from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def internal_directoriesIndex(request):
    context={}

    return render(request,'information_services/internal_directories/index.html',context)

def external_directoriesIndex(request):
    context={}
    return render(request,'information_services/external_directories/index.html',context)

def report_servicesIndex(request):
    context={}
    return render(request,'information_services/report_services/index.html',context)



    