from __future__ import unicode_literals

from django.db import models

# Create your models here.

class User(models.Model):
	name = models.CharField(max_length=20)
	passwd = models.CharField(max_length=200)
	container = models.CharField(max_length=100)

	def __str__(self):
		return self.name



