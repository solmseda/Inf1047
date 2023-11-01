"""
URL configuration for MeuSite project.

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
from django.urls.conf import include
from django.contrib.auth.views import LoginView
from django.contrib.auth.views import LogoutView
from django.contrib.auth.views import PasswordResetView, PasswordResetDoneView
from django.contrib.auth.views import PasswordResetConfirmView, PasswordResetCompleteView
from django.urls.base import reverse_lazy
from MeuSite import views
import MeuApp.views

app_name = 'MeuSite'
urlpatterns = [
    path('', views.home, name='home-page'),
    path('admin/', admin.site.urls),
    path('MeuApp', MeuApp.views.home, name='inicio'),
    path('MeuApp/about', MeuApp.views.about, name='about'),
    path('contatos/', include('contatos.urls')),
    path('seguranca/', views.homeSec, name='sec-home'),
    path('seguranca/registro', views.registro, name='sec-registro'),
    path('seguranca/login/', 
    LoginView.as_view(template_name='seguranca/usuario.html', 
    extra_context={
        'titulo': 'Login',
        'tituloPagina': 'Pagina de Login',
        'textoBotao': 'Login'
    }), name='sec-login'),
    path('logout/', LogoutView.as_view(next_page=reverse_lazy('sec-home'),), name='sec-logout'),
    path('accounts/password_reset/', PasswordResetView.as_view(
        template_name='seguranca/usuario.html', 
        extra_context={
            'titulo': 'Recuperação de Senha',
            'tituloPagina': 'Recuperação de Senha',
            'textoBotao': 'Enviar email'
        },
        success_url=reverse_lazy('sec-password_reset_done'), 
        html_email_template_name='seguranca/password_reset_email.html', 
        subject_template_name='seguranca/password_reset_subject.txt',
        from_email='solmseda@gmai.com.com.br',), 
        name='sec-password_reset'),
    path('accounts/password_reset_done/', PasswordResetDoneView.as_view(
        template_name='seguranca/password_reset_done.html',), 
        name='sec-password_reset_done'),
    path('accounts/password_reset_confirm/<uidb64>/<token>/',PasswordResetConfirmView.as_view(
        template_name='seguranca/password_reset_confirm.html',
        success_url=reverse_lazy('sec-password_reset_complete'),), 
        name='password_reset_confirm'),
    path('accounts/password_reset_complete/', PasswordResetCompleteView.as_view(
        template_name='seguranca/password_reset_complete.html'), 
        name='sec-password_reset_complete'),
]
