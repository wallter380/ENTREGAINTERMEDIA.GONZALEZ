from django.db import models


class Curso(models.Model):

        nombre = models.CharField(max_length=40)
        camada = models.IntegerField(unique=True)
        #activo = models.BooleanField(default=True)
        def __str__(self):

            return f"Curso: {self.nombre}, Camada: {self.camada}"

class Estudiantes(models.Model):

        nombre = models.CharField(max_length=30)
        apellido = models.CharField(max_length=30)
        email = models.EmailField(unique=True)
        #activo = models.BooleanField(default=True)
        def __str__(self):

            return f"Estudiante: {self.nombre} {self.apellido} {self.email}"

class Profesor(models.Model):
        nombre = models.CharField(max_length=30)
        apellido = models.CharField(max_length=30)
        email = models.EmailField(unique=True)
        profesion = models.CharField(max_length=30)
        #activo = models.BooleanField(default=True)
        def __str__(self):

            return f"Profesor: {self.nombre} {self.apellido} {self.email}"

