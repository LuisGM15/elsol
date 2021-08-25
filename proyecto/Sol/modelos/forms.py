from django import forms
from .models import Cuenta
from .models import Entrega
from .models import Actividad
from .models import Respuesta
from .models import Duda
from django.forms import ModelForm, ClearableFileInput, widgets

class CustomClearableFileInput(ClearableFileInput):
    template_with_clear = '<br> <label for=%(clear_checkbox_id)s">%(clear_checkbox_label)s</label> %(clear)s'

class formLogin(forms.ModelForm):
    class Meta:
        model = Cuenta
        fields = ('clave', 'password')

#FORMS PROFESOR
class registroActividadForm(forms.ModelForm):
    class Meta:
        model = Actividad
        fields = ('titulo', 'descripcion', 'fecha_entrega')

class registroRespuestaForm(forms.ModelForm):
    class Meta:
        model = Respuesta
        fields = ('ID_duda', 'contenido')

#FORMS USUARIO
class EntregaActividad(forms.ModelForm):
    class Meta:
        model = Entrega
        fields = ['archivo']
    widgets = {
        'archivo':ClearableFileInput
    }

#Forms para Ambos
class RegistroForoForm(forms.ModelForm):
    class Meta:
        model = Duda
        fields = ('titulo','contenido')
