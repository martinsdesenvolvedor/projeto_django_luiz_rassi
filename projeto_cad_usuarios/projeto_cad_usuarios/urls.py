"""
URL configuration for projeto_cad_usuarios project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app_cad_usuarios import views


urlpatterns = [
    path("admin/", admin.site.urls),
    path('', views.home, name='home'),
    path('usuarios', views.lista_de_usuarios, name='usuarios'),
    path('submit/', views.submit_usuario, name='submit'),
    path('login/', views.login_user, name='login'),
    path('login/submit', views.login_submit, name='login_submit'),
    path('logout/', views.logout_user, name='logout'),
    path('sucesso/', views.pagina_de_sucesso, name='sucesso'),
    
]
