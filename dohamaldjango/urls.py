"""dohamalback URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from check.views import web, dashboard
from rest_framework.authtoken.views import obtain_auth_token
from .views import logout, getGroups
urlpatterns = [
    path('admin/', admin.site.urls),
    path('check/',include('check.urls')),
    path('hamal/',include('hamal.urls')),
    path('tool/',include('tool.urls')),
    path('report/',include('report.urls')),

    path('', web),
    path('dashboard/', dashboard),
    path('token/', obtain_auth_token),
    path('logout/', logout),

    path('getGroups/',getGroups)


]
