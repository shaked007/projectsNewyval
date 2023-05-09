from django.shortcuts import render

from django.http import HttpResponse
from django.http import JsonResponse

from rest_framework import generics
from .models import Check
from .serializers import CheckSerializer, FileCheckSerializer

from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response

from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from dohamaldjango.permissions import IsInGroup_ahmashim, IsInGroup_tehnaim

from rest_framework import status
import io,csv,pandas as pd
import json
class CheckList(generics.ListAPIView):
    permission_classes= [IsAuthenticatedOrReadOnly]
    queryset = Check.objects.all()
    serializer_class = CheckSerializer
    # permission_classes = [IsAuthenticated]

class CheckCreate(generics.CreateAPIView):
    permission_classes= [IsAuthenticated, IsInGroup_tehnaim]
    queryset = Check.objects.all()
    serializer_class = CheckSerializer

class CheckUpdate(generics.UpdateAPIView):
    permission_classes= [IsAuthenticated, IsInGroup_tehnaim]
    queryset = Check.objects.all()
    serializer_class = CheckSerializer

class CheckDelete(generics.DestroyAPIView):
    permission_classes= [IsAuthenticated, IsInGroup_tehnaim]
    queryset = Check.objects.all()
    serializer_class = CheckSerializer

#####
class CheckListByMahlaka(generics.ListAPIView):
    serializer_class = CheckSerializer
    permission_classes= [IsAuthenticatedOrReadOnly]
    def get_queryset(self):
        queryset = Check.objects.filter(mahlaka=self.kwargs['pk'])
        return queryset
#####

@api_view(['GET'])
@permission_classes([IsAuthenticatedOrReadOnly])
def CheckGetByMahlaka(request,*args,**kwargs):
    
    checks = Check.objects.filter(mahlaka=kwargs['pk'])
    data=[]
    for check in checks:
        checkData={
            'Title': check.title,
            'location':check.location,
            'checkId': check.id,
            'mahlaka': check.mahlaka,
        }
        data.append(checkData)
    return Response(data)

@api_view(['GET'])
@permission_classes([IsAuthenticatedOrReadOnly])
def CheckGetByTitle(request,*args,**kwargs):
    
    check = Check.objects.filter(title=kwargs['pk'])
    data=[]
    checkData={
            'Title': check[0].title,
            'location':check[0].location,
            'checkId': check[0].id,
            'mahlaka': check[0].mahlaka,
        }
    data.append(checkData)
    return Response(data)
    
def index(request):
    #return HttpResponse('newval was here')
    return JsonResponse({
        'name': "yuval",
        'age': 20,
    })

def web(request):
    return render(request,'index.html')
def dashboard(request):
    return render(request,'dashboard.html')
def create_mode(data):
    new_check = Check(
        id = data["checkId"],
        title = data["כותרת"],
        location = data["location"],
        mahlaka = data["mahlaka"],
        isCritical = data["isCritical"]
    )
    new_check.save()
class uploadCheck(generics.CreateAPIView):
    serializer_class = FileCheckSerializer
    def post (self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        file = serializer.validated_data['file']
        Check.objects.all().delete()                          #delete all checks!

        reader = pd.read_csv(file)
        for _, row in reader.iterrows():
            create_mode(row)
        return Response({"status":"success"}, status.HTTP_201_CREATED)

class CheckGetByTitleAndMahlaka(generics.ListAPIView):
    serializer_class = CheckSerializer
    permission_classes= [IsAuthenticatedOrReadOnly]
    def get_queryset(self):
        queryset = Check.objects.filter(title=self.kwargs['pk'], mahlaka=self.kwargs['pn'])
        return queryset