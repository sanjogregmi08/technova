import imp
from django.urls import path
from feedback import views

urlpatterns = [
    path('feedback_send',views.send),
    path('feedback_receive',views.receive)
]
