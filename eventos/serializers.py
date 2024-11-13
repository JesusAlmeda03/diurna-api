from rest_framework import serializers
from .models import Eventos, Participantes, Tutores, Estudiantes



class EventosSerializer(serializers.ModelSerializer):
	class Meta:
		model = Eventos
		fields = '__all__'



class ParticipantesSerializer(serializers.ModelSerializer):
	class Meta:
		model = Participantes
		fields = '__all__'



class TutoresSerializer(serializers.ModelSerializer):
	class Meta:
		model = Tutores
		fields = '__all__'



class EstudiantesSerializer(serializers.ModelSerializer):
	class Meta:
		model = Estudiantes
		fields = '__all__'