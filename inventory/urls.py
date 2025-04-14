from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.home, name='home'),  # <-- homepage route
    path('assets/', views.asset_list, name='asset_list'),
    path('assets/new/', views.asset_create, name='asset_create'),
    path('vendors/', views.vendor_list, name='vendor_list'),
    path('vendors/new/', views.vendor_create, name='vendor_create'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
]
