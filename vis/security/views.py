from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def security_policyIndex(request):
    context={}

    return render(request,'security/security_policy/index.html',context)

def access_controlIndex(request):
    context={}
    return render(request,'security/access_control/index.html',context)

def authenticationIndex(request):
    context={}
    return render(request,'security/authentication/index.html',context)

def report_securityIndex(request):
    context={}
    return render(request,'security/report_security/index.html',context)

