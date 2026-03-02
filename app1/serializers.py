from rest_framework import serializers
from .models import members


class MembersSerializer(serializers.ModelSerializer):
    class Meta:
        model = members
        fields = '__all__'