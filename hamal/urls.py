
from django.contrib import admin
from django.urls import path, include
from . import views


urlpatterns = [
    # path('index',views.index,name='index'),
    path('', views.HamalList.as_view()),
    path('create/', views.HamalCreate.as_view()),
    path('update/<int:pk>/', views.HamalUpdate.as_view()),
    path('delete/<int:pk>/', views.HamalDelete.as_view()),
    # ###
    # path('mahlaka/<str:pk>/', views.CheckListByMahlaka.as_view()),
    ###
    # path('mahlaka/<str:pk>/', views.CheckGetByMahlaka),
    # path('name/<str:pk>/', views.CheckGetByTitle),
    path('check/<int:pk>/', views.HamalGetByCheck),
    path('upload/',views.uploadHamal.as_view())
]

