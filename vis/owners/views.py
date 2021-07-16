from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def jismoniyIndex(request):
    context={}

    return render(request,'owners/jismoniy/index.html',context)

def yuridikIndex(request):
    context={}
    return render(request,'owners/yuridik/index.html',context)

def hisobotIndex(request):
    context={}
    return render(request,'owners/hisobot/index.html',context)



    