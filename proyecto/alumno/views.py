from django.shortcuts import render

# Create your views here.
def tareas (request):
    return render (request, 'alumno/tareas.html')

def foro(request):
    return render (request, 'alumno/forodudas.html')