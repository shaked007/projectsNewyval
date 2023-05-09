from .models import Check
from rest_framework import serializers

class CheckSerializer(serializers.ModelSerializer):
    class Meta:
        model = Check
        fields ="__all__"

class FileCheckSerializer(serializers.ModelSerializer):
    file = serializers.FileField()
    class Meta:
        model = Check
        fields =['file']