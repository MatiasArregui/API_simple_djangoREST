from django.db import models

# Create your models here.
class Carreras(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    descripcion = models.TextField()


    def __str__(self):
        return self.nombre


class Cursos(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    descripcion = models.TextField()
    idcarrera = models.ForeignKey(Carreras, on_delete=models.CASCADE)


    def __str__(self):
        return self.nombre


class Alumnos(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    idcurso = models.ForeignKey(Cursos, on_delete=models.CASCADE)


    def __str__(self):
        return self.nombre

