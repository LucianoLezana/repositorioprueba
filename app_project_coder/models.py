
from django.db import models

'''
        Agregando clases:
-Curso (nombre, comision)
-Estudiante (nombre, apellido, email)
-Profesor (nombre, apellido, email, profesion)

'''

class Cursos(models.Model):
    nombre = models.CharField(max_length=120)
    comision = models.IntegerField()

class Estudiantes(models.Model):
    nombre = models.CharField(max_length=120)
    apellido = models.CharField(max_length=120)
    email = models.EmailField()

class Profesores(models.Model):
    nombre = models.CharField(max_length=120)
    apellido = models.CharField(max_length=120)
    email = models.EmailField()
    profesion = models.CharField(max_length=100)

