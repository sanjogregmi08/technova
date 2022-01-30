from django.http import request
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from seller.forms import ProductForm
from django.contrib.auth.models import User
from feedback.models import Feedback
from cart.models import Products
from seller.models import Products1


# Create your views here.


def register(request):
    if request.method == 'POST':
        fullname = request.POST['fullname']
        phonenumber = request.POST['phonenumber']
        email = request.POST['email']
        username = request.POST['username']
        password = request.POST['password']
        user = User.objects.create_user(first_name=fullname,
                                        last_name=phonenumber, email=email, username=username, password=password)
        user.save()
        return redirect('/seller/login')
    return render(request, 'seller/sellerreg.html')


def login(request):
    if request.method == 'POST':
        un = request.POST['username']
        pw = request.POST['password']

        user = auth.authenticate(username=un, password=pw)

        if user is not None:
            auth.login(request, user)
            return redirect('/seller/dashboard')
        else:
            messages.error(request, "bad credentials")
            return redirect('/seller/login')
    return render(request, 'seller/sellerlogin.html')

@login_required(login_url='/seller/login')
def dashboard(request):
    return render(request, 'seller/dashboard.html')

@login_required(login_url='/seller/login')
def addProduct(request):
    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES)
        print(form)
        if form.is_valid():
            try:
                print("valid")
                form.save()
                return redirect("/seller/view_products")
            except:
                print("validation failed")
    else:
        form = ProductForm()
        print("invalid")
    return render(request, 'seller/add_product.html', {'form': form})

@login_required(login_url='/seller/login')
def view_products(request):
    if(request.method == "POST"):
        page = int(request.POST['page'])
        if('prev' in request.POST):
            page = page-1
        if ('next' in request.POST):
            page = page+1
        tempOffSet = page - 1
        offset = tempOffSet*4
        print(offset)
    else:
        offset = 0
        page = 1
    products = Products1.objects.raw(
        "select * from products limit 4 offset % s", [offset])
    pageItem = len(products)
    return render(request, 'seller/viewproduct.html', {'products': products, 'page': page, 'pageItem': pageItem})
@login_required(login_url='/seller/login')
def edit_product(request,p_id):
        try:
            product=Products1.objects.get(id=p_id)
            return render(request, "seller/edit_products.html", {'products':product})
        except:
            print("No Data Found")
            return redirect("/seller/view_products")
@login_required(login_url='/seller/login')            
def update_product(request,p_id):
    products =Products1.objects.get(id=p_id)
    form = ProductForm(request.POST,instance=products)
    if form.is_valid():
        try:
            form.save()
            return redirect("/seller/view_products")
        except:
            print("cannot update")
    return render(request,"seller/edit_products.html",{'products':products})
@login_required(login_url='/seller/login')    
def delete_product(request,p_id):
    try:
        products = Products1.objects.get(id=p_id)
        products.delete()
    except:
        print("no data found")
    return redirect("/seller/view_products")
@login_required(login_url='/seller/login')    
def analytics(request):
    products1 = Products1.objects.all()
    users = User.objects.all()
    feedbacks = Feedback.objects.all()
    cart = Products.objects.all()
    return render(request,'seller/show_analytics.html',{'products':products1,'users':users,'feedbacks':feedbacks,'cart':cart})

