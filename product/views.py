from django.shortcuts import render
from shop import models
import shop
# Create your views here.
def product(request):
    shoes = shop.models.shoe.objects.all()
    return render(request,'product/products.html',{'shoes':shoes})