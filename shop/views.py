from django.shortcuts import render
from .models import Trusted_Partner
# Create your views here.
def index(request):
    prand = Trusted_Partner.objects.all()
    return render(request,'shop/index.html',{'prand':prand})


def about(request):
    return render(request,'shop/about.html')