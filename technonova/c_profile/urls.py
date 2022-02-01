from django.urls import path
from c_profile import views

urlpatterns = [
    path('myprofile',views.myprofile)
]
