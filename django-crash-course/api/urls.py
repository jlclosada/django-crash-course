# api/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TaskViewSet

# Crea un router y registra nuestro viewset con él.
router = DefaultRouter()
router.register(r'tasks', TaskViewSet, basename="task")

# Las URLs de la API son determinadas automáticamente por el router.
urlpatterns = [
    path('', include(router.urls)),
]