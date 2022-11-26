from django.shortcuts import render
from .utilities import get_tenant
from .models import Member

# Create your views here.

def our_team(request):
    tenant=get_tenant(request)
    member=Member.objects.filter(tenant=tenant)
    print(tenant)
    return render(request,"index.html",{"tenant":tenant,"members":member})