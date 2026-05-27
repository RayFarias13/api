from rest_framework import serializers
from .models import AdaptationsModel, ReportsModel, UserModel, AlunoModel

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        fields = '__all__'

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