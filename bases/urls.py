from django.urls import path
from django.contrib.auth import views as auth_views

from bases.views import Home,Registrar,Listar
urlpatterns = [
    path('',Home.as_view(),name='home'),
    path('registrar/',Registrar.as_view(),name='registrar'),
    path('estado/',Listar.as_view(),name='estado'),
    
    path('login/',auth_views.LoginView.as_view(template_name='bases/login.html'),
        name='login'),
    path('logout/',auth_views.LogoutView.as_view(template_name='bases/login.html'),
        name='logout'),        
]