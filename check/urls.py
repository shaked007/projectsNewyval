
from django.contrib import admin
from django.urls import path, include
from . import views


urlpatterns = [
    path('index',views.index,name='index'),
    path('', views.CheckList.as_view()),
    path('create/', views.CheckCreate.as_view()),
    path('update/<int:pk>/', views.CheckUpdate.as_view()),
    path('delete/<int:pk>/', views.CheckDelete.as_view()),
    ###
    path('mahlaka/<str:pk>/', views.CheckGetByMahlaka),
    path('name/<str:pk>/', views.CheckGetByTitle),
    ###
    path('name/<str:pk>/mahlaka/<str:pn>/', views.CheckGetByTitleAndMahlaka.as_view()),
    ###
    path('upload/',views.uploadCheck.as_view()),
    ###
]

