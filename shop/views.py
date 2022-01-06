from django.shortcuts import render
from .models import Trusted_Partner,shoe
# Create your views here.
def index(request):
    prand = Trusted_Partner.objects.all()
    shoes = shoe.objects.all()[:4]
    return render(request,'shop/index.html',{'prand':prand,'shoes':shoes})


def about(request):
    return render(request,'shop/about.html')