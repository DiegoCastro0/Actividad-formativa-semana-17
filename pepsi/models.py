from django.db import models

class Curso(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True, null=True)
    fecha_inicio = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.nombre


class Estudiante(models.Model):
    nombre = models.CharField(max_length=100)
    edad = models.PositiveIntegerField()
    curso = models.ForeignKey(
        Curso,
        on_delete=models.CASCADE,
        related_name="estudiantes",
        null=True,
        blank=True     
    )

    def __str__(self):
        return self.nombre
