from django.urls import path
from customer import views
from django.contrib.auth.views import LogoutView

from technonova import settings


urlpatterns = [
    path("", views.homepage,name='home'),
    path('login',views.login,name='login'),
    path('registration',views.registration,name="registration"),
    path('dashboard',views.dashboard,name='dashboard'),
    path('inventory',views.inventory,name="inventory"),
    path('whats_new',views.whats_new,name='whats_new'),
    path("allproducts",views.allproducts,name="allproducts"),
    path('mouse',views.mouse,name="mouse"),
    path('motherboard',views.motherboard,name="motherboard"),
    path('coolingfan',views.coolingfan,name="coolingfan"),
    path('keyboard',views.keyboard,name="keyboard"),
    path('processor',views.processor,name="processor"),
    path('casing',views.casing,name="casing"),
    path('gpu',views.gpu,name="gpu"),
    path('powersupply',views.powersupply,name="powersupply"),
    path('ram',views.ram,name="ram"),
    path('memory',views.memory,name="memory"),
    path('storage',views.storage,name="storage"),
    path('moniter',views.moniter,name="moniter"),
    path('brands',views.brands,name="brands"),
    path('hp',views.hp,name="hp"),
    path('dell',views.dell,name="dell"),
    path('fantech',views.fantech,name="fantech"),
    path('razer',views.razer,name="razer"),
    path('reddragon',views.reddragon,name="reddragon"),
    path('gigabyte',views.gigabyte,name="gigabyte"),
    path('asus',views.asus,name="asus"),
    path('addtocart',views.addtocart,name="addtocart"),
    path('logout', LogoutView.as_view(next_page=settings.LOGOUT_REDIRECT_URL), name='logout'),
    path('aboutus',views.aboutus,name="aboutus"),
    path('build',views.build,name="build"),
    path('build/processor',views.buildprocessor),
    path('build/coolingfan',views.buildcoolingfan),
    path('build/casing',views.buildcasing),
    path('build/graphics',views.buildgraphics),
    path('build/ram',views.buildram),
    path('build/ssd',views.buildssd),
    path('build/motherboard',views.buildmotherboard),
    path('build/powersupply',views.buildpowersupply),
    path('build/select',views.buildselect),

   
]
