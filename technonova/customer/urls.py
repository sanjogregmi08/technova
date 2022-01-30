from django.urls import path
from customer import views
from django.contrib.auth.views import LogoutView

from technonova import settings


urlpatterns = [
    path("", views.homepage,name='home'),
    path('login',views.login),
    path('registration',views.registration),
    path('dashboard',views.dashboard),
    path('inventory',views.inventory),
    path('whats_new',views.whats_new),
    path("allproducts",views.allproducts),
    path('mouse',views.mouse),
    path('motherboard',views.motherboard),
    path('coolingfan',views.coolingfan),
    path('keyboard',views.keyboard),
    path('processor',views.processor),
    path('casing',views.casing),
    path('gpu',views.gpu),
    path('powersupply',views.powersupply),
    path('ram',views.ram),
    path('memory',views.memory),
    path('storage',views.storage),
    path('moniter',views.moniter),
    path('brands',views.brands),
    path('hp',views.hp),
    path('dell',views.dell),
    path('fantech',views.fantech),
    path('razer',views.razer),
    path('reddragon',views.reddragon),
    path('gigabyte',views.gigabyte),
    path('asus',views.asus),
    path('addtocart',views.addtocart),
    path('logout', LogoutView.as_view(next_page=settings.LOGOUT_REDIRECT_URL), name='logout'),
    path('aboutus',views.aboutus)

   
]
