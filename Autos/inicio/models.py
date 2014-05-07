#encoding:utf-8
from django.db import models
from django.contrib.auth.models import User 

# Create your models here.
class  Auto(models.Model):
	codigo = models.AutoField(max_length=30, primary_key=True)
	nombre = models.CharField(max_length=100)
	precio = models.IntegerField(max_length=100)
	imagen = models.CharField(max_length=100)
	descripcion = models.CharField(max_length=100)
	cilindraje = models.CharField(max_length=100)
	estado = models.BooleanField(null=False)
	def __unicode__(self):
		return self.nombre
