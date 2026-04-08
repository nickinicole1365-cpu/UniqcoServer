from django.db import models

# Create your models here.

class Task(models.Model):
    Product = models.CharField(max_length= 200)
    descripcion = models.TextField()
    ESTADOS = [
        ('Sin previo','Sin previo'),
        ('Grabando','Para Grabar'),
        ('Entregar','Para Entregar'),
    ]
    estado = models.CharField(max_length=20,choices = ESTADOS,default='Sin_previo')


