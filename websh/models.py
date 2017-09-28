from __future__ import unicode_literals
from django.contrib.auth.models import User as BaseUserClass
from django.db import models

# Create your models here.

class User(BaseUserClass):
	server_name = models.CharField(max_length=50)
	server_address = models.CharField(max_length=15)
	



