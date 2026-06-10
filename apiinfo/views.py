from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend

from .models import *

from .serializers import *


'''class UserViewSet(viewsets.ModelViewSet):
    queryset = UserModel.objects.all().order_by('id')
    serializer_class = UserSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['id','user__username','user__email']
'''

class AlunoViewSet(viewsets.ModelViewSet):
    queryset = AlunoModel.objects.all().order_by('id')
    serializer_class = AlunoSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['id','name','course']


class AdaptacaoViewSet(viewsets.ModelViewSet):
    queryset = AdaptationsModel.objects.all().order_by('id')
    serializer_class = AdaptacaoSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['id','student','student__name','description']

    def get_queryset(self):
        queryset = super().get_queryset()

        student_id = self.request.query_params.get('student')

        if student_id:
            queryset = queryset.filter(student_id=student_id)

        return queryset


class RelatorioViewSet(viewsets.ModelViewSet):
    queryset = ReportsModel.objects.all().order_by('id')
    serializer_class = RelatorioSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = [ 'id', 'student', 'student__name','description']

    def get_queryset(self):
        queryset = super().get_queryset()

        student_id = self.request.query_params.get('student')

        if student_id:
            queryset = queryset.filter(student_id=student_id)

        return queryset
    
class User2ViewSet(viewsets.ModelViewSet):
    queryset = User2model.objects.all().order_by('id')
    serializer_class = User2Serializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['id','name','email']

class User3ViewSet(viewsets.ModelViewSet):
    queryset = User3model.objects.all()
    serializer_class = User3Serializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['id', 'username', 'email', 'role']