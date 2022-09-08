from django.shortcuts import render
from django.contrib.auth.decorators import login_required
# Create your views here.


@login_required(login_url='login')
def index(request):
    return render(request, 'expenses/index.html')

def add_despesa(request):
    return render(request, 'expenses/add_despesas.html')
