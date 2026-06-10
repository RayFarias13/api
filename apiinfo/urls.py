from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import *

router = DefaultRouter()
#router.register(r'users', UserViewSet, basename='users')
router.register(r'students', AlunoViewSet, basename='students')
router.register(r'adaptations', AdaptacaoViewSet, basename='adaptations')
router.register(r'reports', RelatorioViewSet, basename='reports')
router.register(r'user', User2ViewSet, basename='user')

urlpatterns = [
    path('', include(router.urls)),

    path('adaptations/students/<int:student_id>/',AdaptacaoViewSet.as_view({'get': 'list_by_student'}),name='adaptacoes-por-aluno'),

    path( 'adaptations/students/<int:student_id>/<int:pk>/',AdaptacaoViewSet.as_view({'put': 'update_by_student','delete': 'destroy_by_student',}),name='adaptacao-aluno-detalhe'),

    path('reports/students/<int:student_id>/', RelatorioViewSet.as_view({'get': 'list_by_student'}),name='relatorios-por-aluno'),

    path('reports/students/<int:student_id>/<int:pk>/',  RelatorioViewSet.as_view({'put': 'update_by_student','delete': 'destroy_by_student',}),name='relatorio-aluno-detalhe'),
]