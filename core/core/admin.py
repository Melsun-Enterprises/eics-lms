from django.contrib import admin
from .models import Student, Course, Payment  # Example models

# Register your models here
admin.site.register(Student)
admin.site.register(Course)
admin.site.register(Payment)
from django.apps import AppConfig

class CoreConfig(AppConfig):
    name = 'core'
