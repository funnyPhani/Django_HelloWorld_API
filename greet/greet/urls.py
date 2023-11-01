"""
URL configuration for greet project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path

from django.http import HttpResponse

# Create your views here.
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import json
@csrf_exempt
def greetUsers(request):
    if request.method == 'POST':

        data = json.loads(request.body)
        name = data.get('name')
        num = data.get("num")
        # dataRange = int(data.get("dataRange"))
        return HttpResponse(f"Hello {name}..! and ur num is  {num}..!")

@csrf_exempt
def greetUserss(request):
    if request.method == 'POST':

        data = json.loads(request.body)
        
        dataRange = int(data.get("dataRange"))
        return JsonResponse({"data":list(range(dataRange))})
    if request.method == 'GET':

        dataRange = int(request.GET.get('dataRange'))
        # http://127.0.0.1:8000/num?dataRange=10
        return JsonResponse({"data":list(range(dataRange))})

from basicApp.views import greetUser,greetUsersss

urlpatterns = [
    path('admin/', admin.site.urls),
    path("",greetUser),
    path("hi",greetUsers),
    path("num",greetUserss),
    path("viewsNum",greetUsersss)
]
