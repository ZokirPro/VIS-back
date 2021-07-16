from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def physical_personIndex(request):
    context={}

    return render(request,'owners/jismoniy/index.html',context)

def juridic_personIndex(request):
    context={}
    return render(request,'owners/yuridik/index.html',context)

def reportIndex(request):
    context={}
    return render(request,'owners/hisobot/index.html',context)



    