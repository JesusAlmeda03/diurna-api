from django.shortcuts import render
from rest_framework import viewsets
from .models import Eventos, Participantes, Tutores, Estudiantes
from .serializers import EventosSerializer, ParticipantesSerializer, TutoresSerializer, EstudiantesSerializer



# Create your views here.
class EventosViewSet(viewsets.ModelViewSet):
	queryset = Eventos.objects.all()
	serializer_class = EventosSerializer



# Create your views here.
class ParticipantesViewSet(viewsets.ModelViewSet):
	queryset = Participantes.objects.all()
	serializer_class = ParticipantesSerializer



# Create your views here.
class TutoresViewSet(viewsets.ModelViewSet):
	queryset = Tutores.objects.all()
	serializer_class = TutoresSerializer



# Create your views here.
class EstudiantesViewSet(viewsets.ModelViewSet):
	queryset = Estudiantes.objects.all()
	serializer_class = EstudiantesSerializer