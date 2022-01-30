from itertools import count
import re
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from cart.forms import cartForm
from cart.models import Products

# Create your views here.
@login_required(login_url='/login')
def mycart(request):
    products =Products.objects.all()
    return render(request,'cart/mycart.html',{'products':products})
@login_required(login_url='/login')    
def clear(request):
    try:
        products =Products.objects.all()
        products.delete()
    except:
        print("cannot delete")
    return redirect("/cart/mycart")   
@login_required(login_url='/login')
def checkout(request):
    products =Products.objects.all()
    
    return render(request,'cart/fund.html',{'products':products})