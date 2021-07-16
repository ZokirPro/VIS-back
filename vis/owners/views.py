from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def fizIndex(request):
    context={}

    return render(request,'owners/fizIndex.html',context)

def yuridIndex(request):
    context={}
    return render(request,'owners/yuridIndex.html',context)
    