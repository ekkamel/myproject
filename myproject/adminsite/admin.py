from django.contrib import admin
from django.apps import AppConfig
from . models import *

# Register your models here.
admin.site.register(Course)
admin.site.register(Instructor)
