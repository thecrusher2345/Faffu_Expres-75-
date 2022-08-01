from pyexpat import model
from tabnanny import verbose
from turtle import update
from django.db import models

# Create your models here.
class Login(models.Model):
    email=models.EmailField(max_length=80, verbose_name="Email")
    contraseña=models.CharField(max_length=20, verbose_name="Contraseña")




