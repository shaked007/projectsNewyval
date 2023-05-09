from .models import Tool
from rest_framework import serializers
import json
class ToolSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tool
        fields ="__all__"

class ViewToolSerializer(serializers.Serializer):

    try:
        TYPES =[tool.type for tool in Tool.objects.all() ]
    except:
        TYPES = ['1','2','3']    
    tool_type = serializers.ChoiceField(choices = TYPES)
    ACTIONS = (
        (0,'add'),
        (1,'update'),
        (2,'delete')
        )
    action = serializers.ChoiceField(choices = ACTIONS)
    BOOLCHECKS_OR_INFO = (
        (0,'boolChecks'),
        (1,'info')
    )
    boolChecks_or_info = serializers.ChoiceField(choices = BOOLCHECKS_OR_INFO)
    key = serializers.CharField()
    boolChecks_value = serializers.ChoiceField(choices = [True, False])
    # info_value = serializers.CharField(required=False)
    info_value = serializers.CharField(default='')
class FileToolSerializer(serializers.ModelSerializer):
    file = serializers.FileField()
    class Meta:
        model = Tool
        fields =['file']