from django.urls import path

from cart import views

urlpatterns =[
    path('mycart',views.mycart),
    path('deletecart',views.clear),
    path('checkout',views.checkout),
    
]