from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import UpdateView

# Create your views here.

def home(request):
    return render(request, 'MeuSite/home.html')

def homeSec(request):
    return render(request, 'seguranca/homeSec.html')

def registro(request):
    if request.method == 'POST':
        formulario = UserCreationForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect('sec-home')
    else:
        formulario = UserCreationForm()
    contexto = {
        'form': formulario, 
        'titulo': "registro",
        'tituloPagina': "Pagina de registro",
        'textoBotao': "registrar"
        }
    return render(request, 'seguranca/usuario.html', contexto)

class MeuUpdateView(UpdateView):
    def get(self, request, pk, *args, **kwargs):
        if request.user.id == pk:
            return super().get(request, pk, args, kwargs)
        else:
            return redirect('sec-home')

def temp(request):
    return