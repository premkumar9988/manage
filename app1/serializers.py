from rest_framework import serializers
from .models import members
from django.contrib.auth.models import User


class MembersSerializer(serializers.ModelSerializer):
    class Meta:
        model = members
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['username', 'password', 'email']

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password'],
            email=validated_data.get('email')
        )
        return user