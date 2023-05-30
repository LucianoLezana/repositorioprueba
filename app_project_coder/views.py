from typing import Dict
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from app_project_coder.models import Cursos, Estudiantes, Profesores
from app_project_coder.forms import *


def inicio (request):
    return render(request, "app_project_coder\inicio.html")  


#Curso-------------------------------------------------------------------------------------------------------------------------------------------------------------------
def cursos(request):
    cursos = Cursos.objects.all()
    return render(request, "app_project_coder\cursos.html", {'cursos': cursos})


def crear_formulario_curso(request):
    if request.method == "POST":
        formulario_curso = form_curso(request.POST)
        print(formulario_curso)
        if formulario_curso.is_valid:
            informacion = formulario_curso.cleaned_data
            cursos = Cursos(nombre=informacion['nombre'], comision=informacion['comision'])
            cursos.save()
            return render(request, "app_project_coder\cursos.html", {"curso_creado":True})

    else:
        formulario_curso = form_curso()
        return render(request, "app_project_coder\crear_cursos.html", {"formulario_curso":formulario_curso})


def busqueda_cursos(request):
    return render(request, "app_project_coder/busqueda_curso.html")


def buscador_cursos(request):
    if request.GET["comision"]:
        comision = request.GET["comision"]
        cursos = Cursos.objects.filter(comision__icontains=comision)
        return render(request, "app_project_coder\cursos.html", {'cursos': cursos})
    else:
        return render(request, "app_project_coder\cursos.html", {'cursos': []})



#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#Estudiantes-------------------------------------------------------------------------------------------------------------------------------------------------------------------

def estudiantes (request):
    estudiantes = Estudiantes.objects.all()
    return render(request, "app_project_coder\estudiantes.html", {'estudiantes': estudiantes})

def crear_formulario_estudiante(request):
    if request.method == "POST":
        formulario_estudiante = form_estudiantes(request.POST)
        print(formulario_estudiante)
        if formulario_estudiante.is_valid:
            informacion = formulario_estudiante.cleaned_data
            estudiantes = Estudiantes(nombre=informacion['nombre'], apellido=informacion['apellido'], email=informacion['email'])
            estudiantes.save()
            return render(request, "app_project_coder\estudiantes.html", {"estudiante_creado": True})
    else:
        formulario_estudiante = form_estudiantes()
        return render(request, "app_project_coder\crear_estudiante.html", {"formulario_estudiante": formulario_estudiante})


#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------


#Profesores-------------------------------------------------------------------------------------------------------------------------------------------------------------------

def profesores (request):
    profesores = Profesores.objects.all()
    return render(request, "app_project_coder\profesores.html",  {'profesores': profesores})
    

def crear_formulario_profesor(request):
    if request.method == "POST":
        formulario_profesor = form_profesores(request.POST)
        print(formulario_profesor)
        if formulario_profesor.is_valid:
            informacion = formulario_profesor.cleaned_data
            profesores = Profesores(nombre=informacion['nombre'], apellido=informacion['apellido'], email=informacion['email'], profesion=informacion['profesion'])
            profesores.save()
            return render(request, "app_project_coder\profesores.html", {"profesor_creado": True})
    else:
        formulario_profesor = form_profesores()
        return render(request, "app_project_coder\crear_profesor.html", {"formulario_profesor": formulario_profesor})
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------
