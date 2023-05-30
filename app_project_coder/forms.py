from socket import fromshare
from django import forms
from .models import Cursos, Estudiantes, Profesores

#Crear formularios para la pagina

#Formulario Cursos:
class form_curso(forms.ModelForm):
    class Meta:
        model = Cursos
        fields = ('nombre', 'comision')

        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control mt-2'}),
            'comision': forms.TextInput(attrs={'class': 'form-control mt-2'}),
        }

#-------------------

#Formulario Estudiantes:

class form_estudiantes(forms.ModelForm):
    class Meta:
        model = Estudiantes
        fields = ('nombre', 'apellido', 'email')

        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control mt-2'}),
            'apellido': forms.TextInput(attrs={'class': 'form-control mt-2'}),
            'email': forms.EmailInput(attrs={'class': 'form-control mt-2'}),
        }

#-------------------

#Formulario Profesores:

class form_profesores(forms.ModelForm):
    class Meta:
        model = Profesores
        fields = ('nombre', 'apellido', 'email', 'profesion')

        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control mt-2'}),
            'apellido': forms.TextInput(attrs={'class': 'form-control mt-2'}),
            'email': forms.EmailInput(attrs={'class': 'form-control mt-2'}),
            'profesion': forms.TextInput(attrs={'class': 'form-control mt-2'}),
        }

#-------------------





