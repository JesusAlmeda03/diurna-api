from django.contrib import admin
from .models import Eventos, Participantes, Tutores, Estudiantes

# Register your models here.
admin.site.register(Eventos)
admin.site.register(Participantes)
admin.site.register(Tutores)
admin.site.register(Estudiantes)


