from rest_framework import serializers
from .models import AdaptationsModel, ReportsModel, User2model, UserModel, AlunoModel

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        fields = '__all__'

class User2Serializer(serializers.ModelSerializer):
    class Meta:
        model = User2model
        fields = 'name', 'email', 'password', 'role'

class AlunoSerializer(serializers.ModelSerializer):
    class Meta:
        model = AlunoModel
        fields = '__all__'

class AdaptacaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = AdaptationsModel
        fields = '__all__'

class RelatorioSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReportsModel
        fields = '__all__'


