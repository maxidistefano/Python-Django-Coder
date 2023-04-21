from django.db import models

# Create your models here.

class Curso(models.Model):

    nombre=models.CharField(max_length=40)
    camada=models.IntegerField()

class Estudiantes(models.Model):
    nombre=models.CharField(max_length=40)
    apellido=models.CharField(max_length=40)
    email=models.EmailField()

class Profesor(models.Model):
    nombre=models.CharField(max_length=40)
    apellido=models.CharField(max_length=40)
    email=models.EmailField()
    profesion=models.CharField(max_length=40)

    
class UserCreationForm(models.Model):
    username=models.CharField(max_length=30)
    password=models.CharField(max_length=30)
    email=models.EmailField()
    