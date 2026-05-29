from django.db import models
from django.contrib.auth.models import User


class Board(models.Model):

    nombre = models.CharField(max_length=100)

    usuario = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.nombre


class Lista(models.Model):

    nombre = models.CharField(max_length=100)

    board = models.ForeignKey(
        Board,
        on_delete=models.CASCADE,
        related_name='listas'
    )

    def __str__(self):
        return self.nombre


class Tarjeta(models.Model):

    PRIORIDADES = [

        ('BAJA', 'Baja'),
        ('MEDIA', 'Media'),
        ('ALTA', 'Alta'),

    ]

    titulo = models.CharField(max_length=200)

    descripcion = models.TextField(blank=True)

    lista = models.ForeignKey(
        Lista,
        on_delete=models.CASCADE,
        related_name='tarjetas'
    )

    creada = models.DateTimeField(
        auto_now_add=True
    )

    fecha_limite = models.DateField(
        null=True,
        blank=True
    )

    prioridad = models.CharField(
        max_length=10,
        choices=PRIORIDADES,
        default='MEDIA'
    )

    COLOR_CHOICES = [
    ('primary', 'Azul'),
    ('success', 'Verde'),
    ('danger', 'Rojo'),
    ('warning', 'Amarillo'),
    ('dark', 'Negro'),
    ('info', 'Celeste'),
    ]

    color = models.CharField(
    max_length=20,
    choices=COLOR_CHOICES,
    default='primary'
    )
    etiqueta = models.CharField(
        max_length=50,
        blank=True
    )

    completada = models.BooleanField(
        default=False
    )

    def __str__(self):

        return self.titulo