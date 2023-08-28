from django.shortcuts import render
#from django.http import HttpResponse

# Create your views here.

def home(request):
    #return HttpResponse("Alo Mundo!", content_type="text/plain")
    return render(request, 'MeuApp/home.html')

def about(request):
    return render(request, 'MeuApp/about.html')