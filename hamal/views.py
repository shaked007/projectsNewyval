from django.shortcuts import render
from .models import Hamal
from rest_framework.decorators import api_view,permission_classes
from rest_framework.response import Response
from rest_framework import generics
from .serializers import HamalSerializer, FileHamalSerializer

from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from dohamaldjango.permissions import IsInGroup_ahmashim, IsInGroup_tehnaim

from check.models import Check
from rest_framework import status
import io,csv,pandas as pd
import json
# Create your views here.

class HamalList(generics.ListAPIView):
    permission_classes= [IsAuthenticatedOrReadOnly]
    queryset = Hamal.objects.all()
    serializer_class = HamalSerializer

class HamalCreate(generics.CreateAPIView):
    permission_classes= [IsAuthenticated, IsInGroup_tehnaim]
    queryset = Hamal.objects.all()
    serializer_class = HamalSerializer

class HamalUpdate(generics.UpdateAPIView):
    permission_classes= [IsAuthenticated, IsInGroup_tehnaim]
    queryset = Hamal.objects.all()
    serializer_class = HamalSerializer

class HamalDelete(generics.DestroyAPIView):
    permission_classes= [IsAuthenticated, IsInGroup_tehnaim]
    queryset = Hamal.objects.all()
    serializer_class = HamalSerializer

@api_view(['GET'])
@permission_classes([IsAuthenticatedOrReadOnly])
def HamalGetByCheck(request,*args,**kwargs):
    
    hamals = Hamal.objects.filter(checkId=kwargs['pk'])
    data=[]
    for hamal in hamals:
        hamalData={
            'Title': hamal.Title,
            'hamalId': hamal.id,
            'checkId': hamal.checkId.id,
        }
        data.append(hamalData)

    return Response(data)
def create_mode(data):
    if Check.objects.filter(id=data["checkId"]).exists():
        new_hamal = Hamal(
            id = data["hamalId"],
            Title = data["כותרת"],
            checkId = Check.objects.filter(id=data["checkId"])[0]
        )
        new_hamal.save()
class uploadHamal(generics.CreateAPIView):
    serializer_class = FileHamalSerializer
    def post (self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        file = serializer.validated_data['file']
        Hamal.objects.all().delete()                          #delete all hamals!

        reader = pd.read_csv(file)
        for _, row in reader.iterrows():
            create_mode(row)
        return Response({"status":"success"}, status.HTTP_201_CREATED)