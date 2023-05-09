
from django.contrib import admin
from django.urls import path, include
from . import views


urlpatterns = [
    # path('index',views.index,name='index'),
    path('', views.ReportList.as_view()),
    path('<int:pk>/',views.ReportRetrieve.as_view()),
    path('create/', views.ReportCreate.as_view()),
    path('update/<int:pk>/', views.ReportUpdate.as_view()),
    path('delete/<int:pk>/', views.ReportDelete.as_view()),
    ####
    path('mail/', views.SendEmail),
    ####
    path('recent/<str:pk>/',views.ReportkGetRecentByCheckName.as_view()),

]

