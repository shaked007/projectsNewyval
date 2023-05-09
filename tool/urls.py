
from django.contrib import admin
from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.ToolList.as_view()),
    path('create/', views.ToolCreate.as_view()),
    path('update/<int:pk>/', views.ToolUpdate.as_view()),
    path('delete/<int:pk>/', views.ToolDelete.as_view()),
    # ###

    path('hamal/<int:pk>/', views.ToolGetByHamal),
    path('id/<int:pk>/', views.ToolGetById),
    ###
    path('updateDetails/', views.updateDetails.as_view()),
    path('upload/',views.uploadTool.as_view()),
]

