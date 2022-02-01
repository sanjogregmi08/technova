import re
from django.shortcuts import redirect, render

from c_profile.forms import DeliveryForm

# Create your views here.
def myprofile(request):
    if(request.method == "POST"):
        form = DeliveryForm(request.POST)
        print(form)
        if form.is_valid:
            try:
                print("valid")
                form.save()
                return  redirect("/dashboard")
            except:
                print("cannot send")
    else:
        form=DeliveryForm()
        print("invalid")
    return render(request,'profile/my_profile.html',{'form':form})