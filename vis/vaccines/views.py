from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def arrivalIndex(request):
    context={}

    return render(request,'vaccines/arrival/index.html',context)

def handbookIndex(request):
    context={}
    return render(request,'vaccines/handbook/index.html',context)

def distributionIndex(request):
    context={}
    return render(request,'vaccines/distribution/index.html',context)

def consumption_rateIndex(request):
    context={}
    return render(request,'vaccines/consumption_rate/index.html',context)

def reportIndex(request):
    context={}
    return render(request,'vaccines/report/index.html',context)


