from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def registration_animalsIndex(request):
    context={}

    return render(request,'vaccination/registration_animals/index.html',context)

def spravochnik_kategoriyaIndex(request):
    context={}
    return render(request,'vaccination/spravochnik_kategoriya/index.html',context)

def spravichnok_svetovIndex(request):
    context={}
    return render(request,'vaccination/spravichnok_svetov/index.html',context)

def schemesIndex(request):
    context={}
    return render(request,'vaccination/schemes/index.html',context)

def registration_vaccinesIndex(request):
    context={}
    return render(request,'vaccination/registration_vaccines/index.html',context)

def report_vaccinationIndex(request):
    context={}
    return render(request,'vaccination/report_vaccination/index.html',context)


