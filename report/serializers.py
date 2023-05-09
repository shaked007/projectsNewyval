from .models import Report
from rest_framework import serializers

class ReportSerializer(serializers.ModelSerializer):
    checkName =  serializers.SerializerMethodField()
    class Meta:
        model = Report
        fields ="__all__"

    def get_checkName(self, obj):
        return obj.checkId.title
