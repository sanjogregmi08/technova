from django.urls import path
from seller import views
from django.contrib.auth.views import LogoutView

from technonova import settings


urlpatterns = [
    path("register", views.register),
    path('login',views.login),
    path('dashboard',views.dashboard),
    path('add_product',views.addProduct),
    path('view_products',views.view_products),
    path('edit_products/<int:p_id>',views.edit_product),
    path('update_products/<int:p_id>',views.update_product),
    path('delete_products/<int:p_id>',views.delete_product),
    path('analytics',views.analytics),
    path('logout', LogoutView.as_view(next_page=settings.LOGOUT_REDIRECT_URL1), name='logout'),
]
