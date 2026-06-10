from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import *

router = DefaultRouter()
router.register(r'students', AlunoViewSet, basename='students')
router.register(r'adaptations', AdaptacaoViewSet, basename='adaptations')
router.register(r'reports', RelatorioViewSet, basename='reports')
router.register(r'user', User2ViewSet, basename='user')  

urlpatterns = [
    path('', include(router.urls)),

    ]