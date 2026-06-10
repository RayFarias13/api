from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken

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









class User2JWTLoginView(APIView):
    permission_classes = []  # público

    def post(self, request):
        email = request.data.get("email")
        password = request.data.get("password")

        if not email or not password:
            return Response(
                {"error": "Email e senha obrigatórios"}, status=status.HTTP_400_BAD_REQUEST
            )

        try:
            user = User2model.objects.get(email=email)
        except User2model.DoesNotExist:
            return Response({"error": "Usuário não encontrado"}, status=status.HTTP_404_NOT_FOUND)

        # Checa senha usando o método do AbstractBaseUser
        if not user.check_password(password):
            return Response({"error": "Senha incorreta"}, status=status.HTTP_401_UNAUTHORIZED)

        # Gera tokens JWT
        refresh = RefreshToken.for_user(user)
        access_token = str(refresh.access_token)
        refresh_token = str(refresh)

        return Response(
            {
                "user": {
                    "id": user.id,
                    "name": user.name,
                    "email": user.email,
                    "role": user.role,
                },
                "access": access_token,
                "refresh": refresh_token,
            },
            status=status.HTTP_200_OK,
        )