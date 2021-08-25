from django.db import models

# Create your models here.
class Rol(models.Model):
    clave = models.AutoField(primary_key=True, verbose_name='Clave')
    nombre = models.TextField(verbose_name='Rol')
    descripcion = models.TextField(verbose_name='Descripción')
    create_at = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de registro')
    update_at = models.DateTimeField(auto_now_add=True, verbose_name='Fecha última actualización')

    class Meta:
        verbose_name = "Rol"
        verbose_name_plural = "Roles"
        ordering = ['-create_at']

    def __str__(self):
        return self.nombre

class Grupo(models.Model):
    id = models.AutoField(primary_key=True, verbose_name='Clave')
    grupo = models.CharField(max_length=2, verbose_name='Grado/grupo')
    create_at = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de registro')
    update_at = models.DateTimeField(auto_now_add=True, verbose_name='Fecha última actualización')

    class Meta:
        verbose_name = "Grupo"
        verbose_name_plural = "Grupos"
        ordering = ['-create_at']

    def __str__(self):
        return self.grupo

class Cuenta(models.Model):
    clave = models.TextField(verbose_name='Clave')
    nombre = models.TextField(verbose_name='Nombre')
    paterno = models.TextField(verbose_name='Apellido paterno')
    materno = models.TextField(verbose_name='Apellido materno')
    correo = models.TextField(verbose_name='Correo electrónico')
    password = models.TextField(verbose_name='Contraseña')
    grupo = models.ForeignKey(Grupo, on_delete=models.CASCADE,verbose_name='Grupo')
    rol = models.ForeignKey(Rol, on_delete=models.CASCADE, verbose_name='Tipo de cuenta')
    create_at = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de registro')
    update_at = models.DateTimeField(auto_now_add=True, verbose_name='Fecha última actualización')

    class Meta:
        verbose_name = "Cuenta"
        verbose_name_plural = "Cuentas"
        ordering = ['-create_at']

    def __str__(self):
        return self.correo

class Actividad(models.Model):
    ID = models.AutoField(primary_key=True, verbose_name='ID')
    ID_profesor = models.TextField(verbose_name='ID profesor')
    nombre_profesor = models.TextField(verbose_name='Profesor')
    titulo = models.TextField(verbose_name='Titulo')
    descripcion = models.TextField(verbose_name='Descripción')
    fecha_entrega =  models.DateTimeField(verbose_name='Fecha de entrega')
    create_at = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de registro')
    update_at = models.DateTimeField(auto_now_add=True, verbose_name='Fecha última actualización') 

    class Meta:
        verbose_name = "Actividad"
        verbose_name_plural = "Actividades"
        ordering = ['-create_at']

    def __str__(self):
        return self.titulo

class Duda(models.Model):
    ID = models.AutoField(primary_key=True, verbose_name='ID')
    ID_usuario = models.TextField(verbose_name='ID usuario')
    nombre_usuario = models.TextField(verbose_name='Autor')
    titulo = models.TextField(verbose_name='Titulo')
    contenido = models.TextField(verbose_name='Contenido de la publicación')
    create_at = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de registro')
    update_at = models.DateTimeField(auto_now_add=True, verbose_name='Fecha última actualización') 

    class Meta:
        verbose_name = "Duda"
        verbose_name_plural = "Dudas"
        ordering = ['-create_at']

    def __str__(self):
        return self.titulo

class Respuesta(models.Model):
    ID = models.AutoField(primary_key=True, verbose_name='ID')
    ID_duda = models.IntegerField(verbose_name='Id Duda')
    ID_usuario = models.TextField(verbose_name='Id usuario')
    nombre_usuario = models.TextField(verbose_name='Autor')
    contenido = models.TextField(verbose_name='Respuesta')
    create_at = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de registro')
    update_at = models.DateTimeField(auto_now_add=True, verbose_name='Fecha última actualización') 

    class Meta:
        verbose_name = "Respuesta"
        verbose_name_plural = "Respuestas"
        ordering = ['-create_at']

    def __str__(self):
        return self.contenido
    
class Entrega(models.Model):
    id = models.AutoField(primary_key=True)
    id_actividad = models.IntegerField()
    actividad = models.TextField(verbose_name='Actividad')
    id_usuario = models.TextField()
    nombre_usuario = models.TextField(verbose_name='Autor')
    archivo = models.FileField(upload_to='archivos', null=True, blank=True)
    create_at = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de registro')
    update_at = models.DateTimeField(auto_now_add=True, verbose_name='Fecha última actualización') 

    class Meta:
        verbose_name = "Entrega"
        verbose_name_plural = "Entregas"
        ordering = ['-create_at']

    """ def __str__(self):
        return self.create_at """
