from django.shortcuts import render

# Create your views here.
def principal(request):
    return render (request, 'contenido/principal.html')

def acceder(request):
    return render (request, 'contenido/login.html')

def acercade(request):
    return render (request, 'contenido/acercade.html')