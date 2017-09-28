from django.contrib import admin
from websh.models import User
from django.contrib.auth.models import User as BaseUserClass

# Register your models here.
admin.site.unregister(BaseUserClass)
admin.site.register(User)