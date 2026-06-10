from rest_framework import serializers
from .models import *
from django_filters import rest_framework as filters


'''class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        fields = '__all__'
'''
class User2Serializer(serializers.ModelSerializer):
    class Meta:
        model = User2model
        fields = '__all__'

class User3Serializer(serializers.ModelSerializer):
    class Meta:
        model = User3model
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


