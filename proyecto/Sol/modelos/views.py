
from django.http.response import FileResponse, HttpResponse
from django.shortcuts import render
from .models import Cuenta, Respuesta
from .models import Actividad
from .models import Duda
from .models import Entrega
from .forms import EntregaActividad, formLogin
from .forms import Entrega
from .forms import registroActividadForm
from .forms import registroRespuestaForm
from .forms import RegistroForoForm
from django.shortcuts import get_object_or_404
#from django.core.checks import messages
from django.contrib import messages

ID_usuario = ""
name = ""
Name_user = ""
sesion_activa = False

# Valifación para el inicio de sesión


def login(request):
    if request.method == 'POST':
        _clave = request.POST['clave']
        _pass = request.POST['password']
        cuenta = Cuenta.objects.raw(
            'SELECT * FROM modelos_cuenta WHERE clave="'+_clave+'" and password ="'+_pass+'"')

        if cuenta:
            cuenta[0].nombre
            for i in cuenta:
                global name
                name = i.nombre
                global ID_usuario
                ID_usuario = i.clave  # Almacena la matricula de la cuenta que haya iniciado sesión
                global sesion_activa
                sesion_activa = True
                global Name_user
                Name_user = i.nombre + " " + i.paterno + " " + i.materno
                if (str(i.rol) == "Profesor"):
                    messages.success(request, "Bienvenido(a) "+name)
                    return render(request, 'modelos/profesor/principal.html')
                else:
                    actividad = Actividad.objects.all()
                    messages.success(request, "Bienvenido(a) "+name)
                    return render(request, 'modelos/alumno/actividades.html', {'actividades': actividad})
        else:
            return render(request, "modelos/pruenanook.html")
    else:
        return render(request, "modelos/pruenanook.html")


def logOut(request):
    global ID_usuario
    ID_usuario = ""
    global sesion_activa
    sesion_activa = False
    global Name_user
    Name_user = ""
    return render(request, 'contenido/principal.html')

# VIEWS DE PROFESOR


def menu(request):
    if sesion_activa:
        return render(request, 'modelos/profesor/principal.html')
    else:
        return render(request, 'contenido/login.html')


def altaActividad(request):
    if sesion_activa:
        return render(request, 'modelos/profesor/registroActividad.html')
    else:
        return render(request, 'contenido/login.html')
    


def registroActividad(request):
    if sesion_activa:
        if request.method == 'POST':
            form = registroActividadForm(request.POST)
            if form.is_valid():
                titulo = request.POST['titulo']
                descripcion = request.POST['descripcion']
                fecha_entrega = request.POST['fecha_entrega']
                insert = Actividad(ID_profesor=ID_usuario, nombre_profesor=Name_user,
                                titulo=titulo, descripcion=descripcion, fecha_entrega=fecha_entrega)
                insert.save()
                actividades = Actividad.objects.filter(ID_profesor=ID_usuario)
                messages.success(request, "Actividad registrada")
                return render(request, 'modelos/profesor/consultaTareas.html', {'actividades': actividades})
        
        messages.success(request, "Error al registrar")
        return render(request, 'modelos/profesor/registroActividad.html')
    else:
        return render(request, 'contenido/login.html')

    


def dudasProfesor(request):
    if sesion_activa:
        dudas = Duda.objects.all()
        return render(request, 'modelos/profesor/dudas.html', {'dudas': dudas})
    else:
        return render(request, 'contenido/login.html')
    


def tareasDetalleProfesor(request, ID):
    if sesion_activa:
        tarea = get_object_or_404(Actividad, ID=ID)
        entregas = Entrega.objects.all()
        #entregas = get_object_or_404(Entrega, id_actividad=ID)
        return render(request, 'modelos/profesor/tareasADetalle.html', {'tarea': tarea, "entregas":entregas})
    else:
        return render(request, 'contenido/login.html')
    


def consultaTareasProfesor(request):
    if sesion_activa:
        actividades = Actividad.objects.filter(ID_profesor=ID_usuario)
        return render(request, 'modelos/profesor/consultaTareas.html', {'actividades': actividades})
    else:
        return render(request, 'contenido/login.html')

    


def responderForoProfesor(request, ID):
    if sesion_activa:
        duda = get_object_or_404(Duda, ID=ID)
        respuestas = Respuesta.objects.all()  # get_object_or_404(Respuesta, ID_duda=ID)
        return render(request, 'modelos/profesor/responderDudas.html', {'duda': duda, 'respuestas': respuestas})
    else:
        return render(request, 'contenido/login.html')

   


def enviarRespuesta(request, ID):
    if sesion_activa:
        dudas = Duda.objects.all()
        respuestas = Respuesta.objects.all()
        duda = get_object_or_404(Duda, ID=ID)

        if request.method == 'POST':
            formR = registroRespuestaForm(request.POST)
            if formR.is_valid():
                ID_duda = request.POST['ID_duda']
                contenido = request.POST['contenido']
                insert = Respuesta(ID_duda=ID_duda, ID_usuario=ID_usuario,
                                contenido=contenido, nombre_usuario=Name_user)
                insert.save()
                return render(request, 'modelos/profesor/responderDudas.html', {'duda': duda, 'respuestas': respuestas})
            else:
                messages.Error(request, "Error al procesar el formulario")
                return render(request, 'modelos/profesor/principal.html')
        else:
            return render(request, 'modelos/profesor/responderDudas.html', {'duda': duda})
    else:
        return render(request, 'contenido/login.html')


    


def foroDudasaDetalle(request):
    if sesion_activa:
        return render(request, 'modelos/alumno/foroDudasDetalle.html')  
    else:
        return render(request, 'contenido/login.html')
    

    

# VIEWS DE ALUMNO


def ActividadesAlumno(request):
    if sesion_activa:
        actividad = Actividad.objects.all()
        return render(request, 'modelos/alumno/actividades.html', {'actividades': actividad})
    else:
        return render(request, 'contenido/login.html')


def SubirActividad(request, ID):
    if sesion_activa:
        actividad = get_object_or_404(Actividad, ID=ID)
        return render(request, 'modelos/alumno/subirActividad.html', {'actividad': actividad})
    else:
        return render(request, 'contenido/login.html')

    


def Entregar(request, ID, actividad):
    if sesion_activa:
        actividades = Actividad.objects.all()
        actividad = get_object_or_404(Actividad, ID=ID)

        if request.method == 'POST':
            form = EntregaActividad(request.POST, request.FILES)
            if form.is_valid():
                archivo = request.FILES['archivo']
                id_actividad = ID
                insert = Entrega(archivo=archivo, id_usuario=ID_usuario,
                                id_actividad=id_actividad, nombre_usuario=Name_user, actividad = actividad)
                insert.save()
                messages.success(request, "Actividad entregada")
                return render(request, 'modelos/alumno/actividades.html', {'actividades': actividades})
            else:
                messages.success(request, "Error al entregar, inténtalo de nuevo mas tarde.")
                return render(request, 'modelos/alumno/subirActividad.html', {'actividad': actividad})
        else:
            return render(request, 'modelos/alumno/subirActividad.html', {'actividad': actividad})
    else:
        return render(request, 'contenido/login.html')


    


def foroDudasAlumno(request):
    if sesion_activa:
        dudas = Duda.objects.all()
        return render(request, 'modelos/alumno/foroDudasA.html', {'dudas': dudas})
    else:
        return render(request, 'contenido/login.html')

    


def foroAltaDudasAlumno(request):
    if sesion_activa:
        return render(request, 'modelos/alumno/altaDudas.html')
    else:
        return render(request, 'contenido/login.html')
    


def registrarDudaForo(request):
    if sesion_activa:
        dudas = Duda.objects.all()

        if request.method == 'POST':
            form = RegistroForoForm(request.POST)
            if form.is_valid():
                titulo = request.POST['titulo']
                contenido = request.POST['contenido']
                insert = Duda(ID_usuario=ID_usuario, nombre_usuario=Name_user,
                            titulo=titulo, contenido=contenido)
                insert.save()
                return render(request, 'modelos/alumno/foroDudasA.html', {'dudas': dudas})

        return render(request, 'modelos/alumno/altaDudas.html')
    else:
        return render(request, 'contenido/login.html')


    

def responderForoAlumno(request, ID):
    if sesion_activa:
        duda = get_object_or_404(Duda, ID=ID)
        respuestas = Respuesta.objects.all()  # get_object_or_404(Respuesta, ID_duda=ID)
        return render(request, 'modelos/alumno/foroDudasDetalle.html', {'duda': duda, 'respuestas': respuestas})
    else:
        return render(request, 'contenido/login.html')

    

def enviarRespuestaAlumno(request, ID):
    if sesion_activa:
        dudas = Duda.objects.all()
        respuestas = Respuesta.objects.all()
        duda = get_object_or_404(Duda, ID=ID)

        if request.method == 'POST':
            formR = registroRespuestaForm(request.POST)
            if formR.is_valid():
                ID_duda = request.POST['ID_duda']
                contenido = request.POST['contenido']
                insert = Respuesta(ID_duda=ID_duda, ID_usuario=ID_usuario,
                                contenido=contenido, nombre_usuario=Name_user)
                insert.save()
                return render(request, 'modelos/alumno/foroDudasDetalle.html', {'duda': duda, 'respuestas': respuestas})
            else:
                messages.Error(request, "Error al procesar el formulario")
                return render(request, 'modelos/alumno/foroDudasA.html', {'dudas': duda})
        else:
            return render(request, 'modelos/alumno/foroDudasDetalle.html', {'duda': duda})
    else:
        return render(request, 'contenido/login.html')


    