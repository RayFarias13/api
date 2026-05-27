from django.urls import path, include
from rest_framework.routers import DefaultRouter


from .views import (
    UserViewSet,
    AlunoViewSet,
    AdaptacaoViewSet,
    RelatorioViewSet
)

router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'alunos', AlunoViewSet)
router.register(r'adaptacoes', AdaptacaoViewSet)
router.register(r'relatorios', RelatorioViewSet)

urlpatterns = [
    

    path('', include(router.urls)),
]