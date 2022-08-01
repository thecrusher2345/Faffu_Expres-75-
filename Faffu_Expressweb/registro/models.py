from django.db import models

# Create your models here.
class registro(models.Model):
    id=models.AutoField(primary_key=True)
    usarid=models.IntegerField(max_length=5)
    nombre=models.CharField(max_length=50, verbose_name='Nombre')
    apellido=models.CharField(max_length=50, verbose_name='Apellido')
    telefono=models.PositiveIntegerField()
    email=models.EmailField(max_length=80)
    contraseña=models.SmallIntegerField(max_length=20)