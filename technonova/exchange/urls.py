from django.urls import path
from exchange import views

urlpatterns = [
    path('exchange_request',views.exchange_request),
    path('exchange_view',views.exchange_view),
    path('refund_view',views.refund_view)

]
