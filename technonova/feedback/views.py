import re
from django.shortcuts import redirect, render

from feedback.form import FeedbackForm
from feedback.models import Feedback
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required(login_url='/login')
def send(request):
    if request.method == "POST":
        form = FeedbackForm(request.POST)
        print(form)
        if form.is_valid:
            try:
                print("valid")
                form.save()
            except:
                print("Cannot Send")
    else:
        form=FeedbackForm()
        print("invalid")
    return render(request,'feedback/feedback_send.html',{'form':form})
@login_required(login_url='/seller/login')    
def receive(request):
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
    feedbacks = Feedback.objects.raw(
        "select * from feedback_feedback limit 4 offset % s", [offset])
    pageItem = len(feedbacks)
    return render(request,'seller/feedback_receive.html',{'feedbacks':feedbacks,'page':page,'pageItem':pageItem})