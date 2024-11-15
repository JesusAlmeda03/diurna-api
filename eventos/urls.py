from django.urls import path, include
from rest_framework import routers
from eventos import views

routers=routers.DefaultRouter()
routers.register(r'eventos', views.EventosViewSet)
routers.register(r'participantes', views.ParticipantesViewSet)
routers.register(r'tutores', views.TutoresViewSet)
routers.register(r'estudiantes', views.EstudiantesViewSet)

urlpatterns = [
	path('', include(routers.urls))
]


#618 8380683 Maestra Alaba Sandoval