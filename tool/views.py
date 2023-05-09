from django.shortcuts import render
#
from .models import Tool
from rest_framework.decorators import api_view,permission_classes
from rest_framework.response import Response
from rest_framework import generics
from .serializers import ToolSerializer,ViewToolSerializer, FileToolSerializer
from rest_framework import serializers
from rest_framework.views import APIView

from .actions import updateValue

from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated, IsAdminUser
from dohamaldjango.permissions import IsInGroup_ahmashim, IsInGroup_tehnaim
from rest_framework.authentication import SessionAuthentication

from .models import Tool
from hamal.models import Hamal
from rest_framework import status
import io,csv,pandas as pd
import json

import math
###

# Create your views here.
class ToolList(generics.ListAPIView):
    permission_classes= [IsAuthenticatedOrReadOnly]
    queryset = Tool.objects.all()
    serializer_class = ToolSerializer

class ToolCreate(generics.CreateAPIView):
    permission_classes= [IsAuthenticated, IsInGroup_ahmashim]

    queryset = Tool.objects.all()
    serializer_class = ToolSerializer

class ToolUpdate(generics.UpdateAPIView):
    permission_classes= [IsAuthenticated, IsInGroup_ahmashim]

    queryset = Tool.objects.all()
    serializer_class = ToolSerializer

class ToolDelete(generics.DestroyAPIView):
    permission_classes= [IsAuthenticated, IsInGroup_ahmashim]

    queryset = Tool.objects.all()
    serializer_class = ToolSerializer
@api_view(['GET'])
@permission_classes([IsAuthenticatedOrReadOnly])

def ToolGetByHamal(request,*args,**kwargs):
    
    Tools = Tool.objects.filter(hamalId=kwargs['pk'])
    data=[]
    for tool in Tools:
        ToolData={
            'delayCause': tool.delayCause,
            'comments' : tool.comments,
            'Title': tool.Title,
            'type': tool.type,
            'hamalId': tool.hamalId.id,

            'ip': tool.ip,
            'details':{
                'boolChecks': tool.boolChecks,
                'info':tool.info
            },
            'id': tool.id
           
        }
        data.append(ToolData)

    return Response(data)


@api_view(['GET'])
@permission_classes([IsAuthenticatedOrReadOnly])

def ToolGetById(request,*args,**kwargs):
    
    tool = Tool.objects.filter(id=kwargs['pk'])[0]
    data={
            'delayCause': tool.delayCause,
            'Title': tool.Title,
            'type': tool.type,
            'hamalId': tool.hamalId.id,

            'ip': tool.ip,
            'details':{
                'boolChecks': tool.boolChecks,
                'info':tool.info
            }
    }
    return Response(data)
###
class updateDetails(APIView):
    authentication_classes = [SessionAuthentication]
    permission_classes= [IsAdminUser]
    serializer_class = ViewToolSerializer
    def post(self,request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            data = serializer.data
            updateValue(data)
        else:
            data = serializer.errors
        return Response(data)

def create_mode(data):
    # print(data)
    for key, value in data.items():
        try:
            if math.isnan(value):
                data[key] = None
        except:
            pass
    # print(data)
    # print(data["delayCause"],type(data["delayCause"]),bool(data["delayCause"]),math.isnan(data["delayCause"]))
    details = json.loads(data['details'])
    if Hamal.objects.filter(id=data["hamalId"]).exists():
        new_tool = Tool(
            # and math.isnan(data["comments"])
            # comments= None if type(data["comments"])==float else  data["comments"],
            comments=  data["comments"],
            #delayCause= None if math.isnan(data["delayCause"]) else  data["delayCause"],
            delayCause= data["delayCause"],

            Title=data["Title"],
            type=data["type"],
            hamalId = Hamal.objects.filter(id=data["hamalId"])[0],
            #ip=  None if math.isnan(data["ip"]) else  data["ip"],
            # ip=  None if  type(data["ip"])==float else  data["ip"],
            ip = data["ip"],
            boolChecks=details["boolChecks"],
            info=details["info"],
#            id = data["hamalId"],
        )
        new_tool.save()
        # print(new_tool)
class uploadTool(generics.CreateAPIView):
    serializer_class = FileToolSerializer
    def post (self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        file = serializer.validated_data['file']
        reader = pd.read_csv(file)
        Tool.objects.all().delete()                          #delete all tools!
        for _, row in reader.iterrows():
            create_mode(row)
        return Response({"status":"success"}, status.HTTP_201_CREATED)