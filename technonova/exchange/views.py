from django.shortcuts import render

from exchange.forms import ExchangeForm
from exchange.models import Exchange
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required(login_url='/login')
def exchange_request(request):
    if request.method == 'POST':
        form = ExchangeForm(request.POST)
        print(form)
        if form.is_valid:
            try:
                print("valid")
                form.save()
            except:
                print('cannot send')
    else:
        form=ExchangeForm()
        print('invalid')

    return render(request,'exchange/exchange_request.html',{'form':form})
@login_required(login_url='/seller/login')    
def exchange_view(request):
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
    exchanges = Exchange.objects.raw(
        "select * from exchange_exchange where type='exchange' limit 4 offset % s", [offset])
    pageItem = len(exchanges)
    return render(request,'exchange/exchange_view.html',{'exchanges':exchanges,'page':page,'pageItem':pageItem})
@login_required(login_url='/seller/login')    
def refund_view(request): 
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
    exchanges = Exchange.objects.raw(
        "select * from exchange_exchange where type='refund' limit 4 offset % s", [offset])
    pageItem = len(exchanges)
    return render(request,'exchange/refund.html',{'exchanges':exchanges,'page':page,'pageItem':pageItem})