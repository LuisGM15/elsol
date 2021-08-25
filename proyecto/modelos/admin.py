from django.contrib import admin
from .models import Rol
from .models import Cuenta
from .models import Grupo 
from .models import Duda
from .models import Respuesta
from .models import Actividad
from .models import Entrega

# Register your models here.
class AdministrarRol(admin.ModelAdmin):
    readonly_fields = ('clave','create_at', 'update_at')
    list_display = ('clave', 'nombre', 'descripcion', 'create_at')
    search_fields = ('clave', 'nombre')

class AdministrarCuenta(admin.ModelAdmin):
    readonly_fields = ('create_at', 'update_at')
    list_display = ('clave', 'paterno', 'materno', 'nombre', 'correo', 'rol', 'grupo')
    date_hierarchy = ('create_at')
    list_filter = ('rol','grupo')
    search_fields = ('clave', 'nombre')

class AdministrarGrupo(admin.ModelAdmin):
    readonly_fields = ('id', 'create_at', 'update_at')
    list_display = ('id', 'grupo', 'create_at')
    search_fields = ('id', 'grupo')

class AdministrarDuda(admin.ModelAdmin):
    readonly_fields = ('create_at', 'update_at')
    list_display = ('titulo', 'contenido', 'create_at', 'nombre_usuario')
    date_hierarchy = ('create_at')
    list_filter = ('create_at','nombre_usuario')
    search_fields = ('titulo', 'contenido', 'create_at', 'nombre_usuario')

class AdministrarRespuesta(admin.ModelAdmin):
    readonly_fields = ('create_at', 'update_at')
    list_display = ('contenido', 'nombre_usuario', 'create_at')
    date_hierarchy = ('create_at')
    list_filter = ('create_at','nombre_usuario')
    search_fields = ('contenido', 'create_at', 'nombre_usuario')

class AndimistrarActividades(admin.ModelAdmin):
    readonly_fields = ('create_at', 'update_at')
    list_display = ('titulo', 'descripcion', 'nombre_profesor','create_at')
    date_hierarchy = ('create_at')
    list_filter = ('create_at','nombre_profesor')
    search_fields = ('descripcion', 'create_at', 'nombre_profesor')

class AdministrarEntregas(admin.ModelAdmin):
    readonly_fields = ('create_at', 'update_at')
    list_display = ('actividad', 'nombre_usuario', 'archivo','create_at')
    date_hierarchy = ('create_at')
    list_filter = ('create_at','nombre_usuario')
    search_fields = ('actividad', 'create_at', 'nombre_usuario')

admin.site.register(Rol, AdministrarRol)
admin.site.register(Cuenta, AdministrarCuenta)
admin.site.register(Grupo, AdministrarGrupo)
admin.site.register(Duda, AdministrarDuda)
admin.site.register(Respuesta, AdministrarRespuesta)
admin.site.register(Actividad, AndimistrarActividades)
admin.site.register(Entrega, AdministrarEntregas)
