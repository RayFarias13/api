from rest_framework import serializers
from .models import *
from django_filters import rest_framework as filters


'''class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        fields = '__all__'
'''
class User2Serializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User2model
        exclude = ['last_login','is_superuser', 'is_staff', 'groups', 'user_permissions']
        #fields = '__all__'

        def create(self, validated_data):
            password = validated_data.pop('password')
            user = User2model(**validated_data)
            user.set_password(password)
            user.save()
            return user
        
        def update(self, instance, validated_data):
            password = validated_data.pop('password', None)
            for attr, value in validated_data.items():
                setattr(instance, attr, value)
            if password:
                instance.set_password(password)
            instance.save()
            return instance


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


