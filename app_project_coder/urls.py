from django.urls import path
from app_project_coder import views

urlpatterns = [

    path('', views.inicio, name="Inicio"),
    
    # PATH DE CURSOS---------------------------------------------------------------------------
    path('cursos/', views.cursos, name="Cursos"),
    path('crear_cursos/', views.crear_formulario_curso, name="crear_cursos"),
    path('buscar_curso/', views.busqueda_cursos, name="buscar_curso"),
    path('busqueda_curso/', views.buscador_cursos, name="busqueda_curso"),
    #------------------------------------------------------------------------------------------
    
    # PATH DE ESTUDIANTES---------------------------------------------------------------------------
    path('estudiantes/', views.estudiantes, name="Estudiantes"),
    path('crear_estudiante/', views.crear_formulario_estudiante, name="crear_estudiante"),

    #------------------------------------------------------------------------------------------
    
    # PATH DE PROFESORES---------------------------------------------------------------------------
    path('profesores/', views.profesores, name="Profesores"),
    path('crear_profesor/', views.crear_formulario_profesor, name="crear_profesor"),

    #------------------------------------------------------------------------------------------

]