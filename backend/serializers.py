from rest_framework import serializers
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from .models import UserLocations

class LoginUserSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

    def validate(self, data):
        user = authenticate(**data)
        if user and user.is_active:
            return user
        raise serializers.ValidationError("Invalid Credentials.", code=401)


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username')

class ListUserLocationsSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserLocations
        fields = '__all__'

class CreateUserLocationsSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserLocations
        fields = ('latitude', 'longitude',)