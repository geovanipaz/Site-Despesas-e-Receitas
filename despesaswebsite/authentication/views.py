from curses.ascii import isalnum
from django.shortcuts import render
from django.views import View
from django.contrib.auth.models import User
import json
from django.http import JsonResponse
# Create your views here.

class UsernameValidationView(View):
    def post(self, request):
        data = json.loads(request.body)
        username = data['username']
        
        if not str(username).isalnum():
            return JsonResponse({'username_erro':'Username deve conter apenas '
                                 'caracteres alfanumericos'}, status=400)
            
        if User.objects.filter(username=username).exists():
            return JsonResponse({'username_erro':'Username já está sendo usado. '
                                 'Escolha outro'}, status=409)
        return JsonResponse({'username_valid': True})

class RegistrationView(View):
    def get(self, request):
        return render(request,'authentication/register.html')
    
