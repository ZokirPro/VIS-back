from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def user_adminstrationIndex(request):
    context={}

    return render(request,'adminstration_system/user_adminstration/index.html',context)

def user_rightsIndex(request):
    context={}
    return render(request,'adminstration_system/user_rights/index.html',context)

def auditIndex(request):
    context={}
    return render(request,'adminstration_system/audit/index.html',context)

def archive_restoreIndex(request):
    context={}
    return render(request,'adminstration_system/archive_restore/index.html',context)

def report_adminstrationIndex(request):
    context={}
    return render(request,'adminstration_system/report_adminstration/index.html',context)


