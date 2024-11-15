from rest_framework import serializers
from usuarios.models import Usuarios
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuarios
        fields = ['id', 'email', 'username', 'last_name', 'password', 'is_superuser', 'is_staff']


class UserRegisterSerializer(serializers.ModelSerializer):  
    class Meta:
        model = Usuarios
        fields = ['id', 'email', 'username', 'last_name', 'password']

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        is_staff = validated_data.pop('is_staff', True)  # Obtén is_staff del validated_data
        instance = self.Meta.model(**validated_data)

        if password is not None:
            instance.set_password(password)
        instance.is_staff = is_staff  # Asigna el valor de is_staff
        instance.save()

        return instance
        
class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        # Llama al método original para obtener los tokens
        data = super().validate(attrs)

        # Agrega los datos del usuario autenticado usando tu UserSerializer
        user_data = UserSerializer(self.user).data
        
        # Combina los datos del token con los datos del usuario
        data.update(user_data)

        return data