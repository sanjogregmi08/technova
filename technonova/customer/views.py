import re
from django.contrib import auth
from django.shortcuts import redirect, render
from pkg_resources import register_finder

from customer.form import CustomerForm
from customer.models import Customer
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from seller.models import Products1
from cart.forms import cartForm



def homepage(request):
    return render(request, 'customer/home2.html')


def login(request):
    if request.method == 'POST':
        un = request.POST['username']
        pw = request.POST['password']

        user = auth.authenticate(username=un, password=pw)

        if user is not None:
            auth.login(request, user)
            return redirect('/dashboard')
        else:
            messages.error(request, "bad credentials")
            return redirect('/login')

    return render(request, 'customer/login.html')


def registration(request):
    if request.method == 'POST':
        fullname = request.POST['fullname']
        phonenumber = request.POST['phonenumber']
        email = request.POST['email']
        username = request.POST['username']
        password = request.POST['password']
        user = User.objects.create_user(first_name=fullname,
                                        last_name=phonenumber, email=email, username=username, password=password)
        user.save()
        return redirect('login')
    return render(request, 'customer/registration.html')

@login_required(login_url='/login')
def dashboard(request):
    return render(request, 'customer/dashboard.html')
@login_required(login_url='/login')
def inventory(request):
    return render(request,'customer/inventory.html')

@login_required(login_url='/login')  
def whats_new(request):
    products =Products1.objects.all()
    return render(request,'customer/what_new.html',{'products':products})
@login_required(login_url='/login')    
def allproducts(request):
    products = Products1.objects.all()
    return render(request,'customer/allproducts.html',{'products':products})
@login_required(login_url='/login')
def mouse(request):
    products=Products1.objects.filter(item="mouse")
    return render(request,"customer/products/mouse.html",{'products':products})
@login_required(login_url='/login')
def motherboard(request):
    products=Products1.objects.filter(item="motherboard")
    return render(request,"customer/products/Motherboard.html",{'products':products})
@login_required(login_url='/login')
def coolingfan(request):
    products=Products1.objects.filter(item="cooling fan")
    return render(request,"customer/products/coolingfan.html",{'products':products})
@login_required(login_url='/login')
def keyboard(request):
    products=Products1.objects.filter(item="keyboard")
    return render(request,"customer/products/keyboard.html",{'products':products})
@login_required(login_url='/login')
def processor(request):
    products=Products1.objects.filter(item="processor")
    return render(request,"customer/products/processor.html",{'products':products})
@login_required(login_url='/login')
def casing(request):
    products=Products1.objects.filter(item="casing")
    return render(request,"customer/products/casing.html",{'products':products})
@login_required(login_url='/login')
def gpu(request):
    products=Products1.objects.filter(item="gpu")
    return render(request,"customer/products/gpu.html",{'products':products})
@login_required(login_url='/login')
def powersupply(request):
    products=Products1.objects.filter(item="powersupply")
    return render(request,"customer/products/powersupply.html",{'products':products})
@login_required(login_url='/login')
def ram(request):
    products=Products1.objects.filter(item="ram")
    return render(request,"customer/products/ram.html",{'products':products})
@login_required(login_url='/login')
def memory(request):
    products=Products1.objects.filter(item="memory")
    return render(request,"customer/products/memory.html",{'products':products})
@login_required(login_url='/login')
def storage(request):
    products=Products1.objects.filter(item="storage")
    return render(request,"customer/products/storage.html",{'products':products})
@login_required(login_url='/login')
def moniter(request):
    products=Products1.objects.filter(item="moniter")
    return render(request,"customer/products/moniter.html",{'products':products})
@login_required(login_url='/login')
def brands(request):
    products = Products1.objects.all()
    return render(request,'customer/brands.html',{'products':products})
@login_required(login_url='/login')
def hp(request):
    products=Products1.objects.filter(brand="hp")
    return render(request,"customer/brands/hp.html",{'products':products})
@login_required(login_url='/login')
def dell(request):
    products=Products1.objects.filter(brand="dell")
    return render(request,"customer/brands/dell.html",{'products':products})
@login_required(login_url='/login')
def fantech(request):
    products=Products1.objects.filter(brand="fantech")
    return render(request,"customer/brands/fantech.html",{'products':products})
@login_required(login_url='/login')
def razer(request):
    products=Products1.objects.filter(brand="razer")
    return render(request,"customer/brands/razer.html",{'products':products})
@login_required(login_url='/login')
def reddragon(request):
    products=Products1.objects.filter(brand="reddragon")
    return render(request,"customer/brands/reddragon.html",{'products':products})
@login_required(login_url='/login')
def gigabyte(request):
    products=Products1.objects.filter(brand="gigabyte")
    return render(request,"customer/brands/gigabyte.html",{'products':products})
@login_required(login_url='/login')
def asus(request):
    products=Products1.objects.filter(brand="asus")
    return render(request,"customer/brands/asus.html",{'products':products})
@login_required(login_url='/login')
def addtocart(request):
    if request.method == "POST":
        print(request.method)
        print('hello')
        form = cartForm(request.POST, request.FILES)
        print(form)
        if form.is_valid():
            try:
                print("valid")
                form.save()
            except:
                print("validation failed")
    else:
        form = cartForm()
        print("invalid") 
    return redirect("/allproducts")
@login_required(login_url='/login')
def aboutus(request):
    return render(request,'customer/aboutus.html ')
@login_required(login_url='/login')
def build(request):
    return render(request,'customer/build.html')
def buildprocessor(request):
    products=Products1.objects.filter(item="processor")
    return render(request,'build/processor.html',{'products':products})
def buildselect(request):
    if request.method == "POST":
        print(request.method)
        print('hello')
        form = cartForm(request.POST, request.FILES)
        print(form)
        if form.is_valid():
            try:
                print("valid")
                form.save()
            except:
                print("validation failed")
    else:
        form = cartForm()
        print("invalid") 
    return redirect("/build")
def buildcoolingfan(request):
    products=Products1.objects.filter(item="cooling fan")
    return render(request,'build/coolinfan.html',{'products':products})
def buildcasing(request):
    products =Products1.objects.filter(item='casing')
    return render(request,'build/casing.html',{'products':products})
def buildgraphics(request):
    products =Products1.objects.filter(item='gpu')
    return render(request,'build/graphics.html',{'products':products})
def buildram(request):
    products =Products1.objects.filter(item='ram')
    return render(request,'build/ram.html',{'products':products})
def buildssd(request):
    products =Products1.objects.filter(item='memory')
    return render(request,'build/ssd.html',{'products':products})
def buildmotherboard(request):
    products =Products1.objects.filter(item='motherboard')
    return render(request,'build/motherboard.html',{'products':products})
def buildpowersupply(request):
    products =Products1.objects.filter(item='power supply')
    return render(request,'build/powersupply.html',{'products':products})