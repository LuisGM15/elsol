
from django.contrib import admin
from django.urls import path
from contenido import views as views_contenido
from alumno import views as views_alumno
from modelos import views as views_modelos
from django.conf import settings

urlpatterns = [
    #RUTAS PRINCIPALES
    path('admin/', admin.site.urls),
    path('', views_contenido.principal, name='Inicio'),
    path('acceder/', views_contenido.acceder, name='Acceder'),
    path('acerca/', views_contenido.acercade, name='Acerca'),
    path('tareas/', views_alumno.tareas, name='Tareas'),
    path('forodudas/', views_alumno.foro, name='Foro'), 

    #RUTA DEL LOGIN
    path('login/', views_modelos.login, name="Login"),
    path('logout', views_modelos.logOut, name ="LogOut"),
    #RUTAS DE PROFESOR
    path('profesor/Menu', views_modelos.menu, name="Menu"),
    path('profesor/ActividadAlta', views_modelos.altaActividad, name="AltaActividad"),
    path('profesor/Dudas', views_modelos.dudasProfesor, name="DudasProfesor"),
    path('profesor/ResponderForo/<int:ID>', views_modelos.responderForoProfesor, name="PResponder"),
    path('profesor/EnviarRespuesta/<int:ID>', views_modelos.enviarRespuesta, name="EnviarRespuesta"),
    path('profesor/TareasDetalle/<int:ID>', views_modelos.tareasDetalleProfesor, name="TareasDetalleProfesor"),
    path('profesor/ConsultaTareas', views_modelos.consultaTareasProfesor, name="ConsultaTareasProfesor"),
    path('profesor/AltaActividad', views_modelos.registroActividad, name="AltaActividadEnviar"),
    

    #RUTAS DE ALUMNO
    path('alumno/Actividades', views_modelos.ActividadesAlumno, name="Actividades"),
    path('alumno/SubirActividad/<int:ID>', views_modelos.SubirActividad, name="SubirActividad"),
    path('alumno/Entrega/<int:ID><str:actividad>', views_modelos.Entregar, name="Entrega"),
    path('alumno/ForoDudas', views_modelos.foroDudasAlumno, name='Foro'),
    path('alumno/ForoAltaDudas', views_modelos.foroAltaDudasAlumno, name='AltaDudas'),
    path('alumno/ForoDudasDetalle', views_modelos.foroDudasaDetalle, name='ForoDetalles'),
    path('AltaForo', views_modelos.registrarDudaForo, name="AltaForo"),
    path('alumno/ResponderForo/<int:ID>', views_modelos.responderForoAlumno, name="AResponder"),
    path('alumno/EnviarRespuesta/<int:ID>', views_modelos.enviarRespuestaAlumno, name="EnviarRespuestaAlumno"),

]

if settings.DEBUG:
    from django.conf.urls.static import static 
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
