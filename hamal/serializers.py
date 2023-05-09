from .models import Hamal
from rest_framework import serializers

class HamalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hamal
        fields ="__all__"
class FileHamalSerializer(serializers.ModelSerializer):
    file = serializers.FileField()
    class Meta:
        model = Hamal
        fields =['file']