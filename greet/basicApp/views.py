
from django.http import HttpResponse

# Create your views here.
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import json

@csrf_exempt
def greetUser(request):
    if request.method == 'POST':

        data = json.loads(request.body)
        name = data.get('name')
        return HttpResponse(f"Hello {name}..!")
    

@csrf_exempt
def greetUsersss(request):
    if request.method == 'POST':

        data = json.loads(request.body)
        
        dataRange = int(data.get("dataRange"))
        return JsonResponse({"data":list(range(dataRange))})