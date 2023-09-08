from django.urls.conf import path
from contatos import views

app_name = 'contatos'

urlpatterns = [
    path('', views.ContatoListView.as_view(), name='home-contatos'),
    path('lista/', views.ContatoListView.as_view(), name='lista-contatos'),
    path('cria/', views.ContatoCreateView.as_view(), name='cria-contatos'),
    path('atualiza/<int:pk>/', views.ContatoUpdateView.as_view(), name='atualiza-contato'),
    path('apaga/<int:pk>/', views.ContatoDeleteView.as_view(), name='apaga-contato'),
] 