from curses.ascii import isalnum
from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.models import User
import json
from django.http import JsonResponse
from django.core.validators import validate_email, EmailValidator
from django.core.exceptions import ValidationError
from django.contrib import messages
from django.contrib import auth


#from validate_email import validate_email
# Create your views here.

class EmailValidationView(View):
    def post(self, request):
        data = json.loads(request.body)
        email = data['email']
        
        #passa se email é válido
        try:
            validate_email(email)
        except ValidationError:
            return JsonResponse({'email_erro':'Email inválido'
                                 ''}, status=400)
            
        if User.objects.filter(email=email).exists():
            return JsonResponse({'email_erro':'Email já está sendo usado. '
                                 'Escolha outro'}, status=409)
        return JsonResponse({'email_valid': True})

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
    def post(self, request):
        #GET USER DATA
        #validar
        #criar uma nova conta
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        
        context = {
            'campos':request.POST
        }
        
        if not User.objects.filter(username=username).exists():
            if not User.objects.filter(email=email).exists():
                if len(password)<5:
                    messages.error(request, 'Senha muito curta')
                    return render(request,'authentication/register.html', context)
                user = User.objects.create_user(username=username, password=password)
                user.set_password(password)
                messages.success(request,'Usuário criado com sucesso.')
                return render(request,'authentication/register.html')
        
        return render(request,'authentication/register.html')
    

class LoginView(View):
    def get(self, request):
        return render(request, 'authentication/login.html')
    
    def post(self, request):
        username = request.POST['username']
        password = request.POST['password']
        
        if username and password:
            user = auth.authenticate(username=username, password=password)
            
            if user:
                if user.is_active:
                    auth.login(request, user)
                    messages.success(request,'Bem Vindo '+user.username+
                                     ' Agora você está logado')
                messages.error(request,'Conta não ativada')
                return redirect('despesas')
            messages.error('Credenciais Inválidas')
            return render(request, 'authentication/login.html')
        messages.error(request,'Preencha os campos')
        return render(request, 'authentication/login.html')
        
        
class LogoutView(View):
    def post(self,request):
        auth.logout(request)
        messages.success(request, 'Você saiu.')
        return redirect('login')