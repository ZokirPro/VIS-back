from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def registration_vaccinated_animalsIndex(request):
    context={}

    return render(request,'diagnostics/registration_vaccinated_animals/index.html',context)

def test_resultsIndex(request):
    context={}
    return render(request,'diagnostics/test_results/index.html',context)

def recommendationsIndex(request):
    context={}
    return render(request,'diagnostics/recommendations/index.html',context)

def report_diagnosticsIndex(request):
    context={}
    return render(request,'diagnostics/report_diagnostics/index.html',context)

