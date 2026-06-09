from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import (
    UserViewSet,
    AlunoViewSet,
    AdaptacaoViewSet,
    RelatorioViewSet,
)

router = DefaultRouter()
router.register(r'users', UserViewSet, basename='users')
router.register(r'alunos', AlunoViewSet, basename='alunos')
router.register(r'adaptacoes', AdaptacaoViewSet, basename='adaptacoes')
router.register(r'relatorios', RelatorioViewSet, basename='relatorios')

urlpatterns = [
    path('', include(router.urls)),

    path(
        'adaptacoes/aluno/<int:student_id>/',
        AdaptacaoViewSet.as_view({'get': 'list_by_student'}),
        name='adaptacoes-por-aluno'
    ),

    path(
        'adaptacoes/<int:student_id>/<int:pk>/',
        AdaptacaoViewSet.as_view({
            'put': 'update_by_student',
            'delete': 'destroy_by_student',
        }),
        name='adaptacao-aluno-detalhe'
    ),

    path(
        'relatorios/aluno/<int:student_id>/',
        RelatorioViewSet.as_view({'get': 'list_by_student'}),
        name='relatorios-por-aluno'
    ),

    path(
        'relatorios/<int:student_id>/<int:pk>/',
        RelatorioViewSet.as_view({
            'put': 'update_by_student',
            'delete': 'destroy_by_student',
        }),
        name='relatorio-aluno-detalhe'
    ),
]