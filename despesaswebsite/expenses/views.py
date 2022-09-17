from multiprocessing import context
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Category, Expense
# Create your views here.


@login_required(login_url='login')
def index(request):
    categories = Category.objects.all()
    expenses = Expense.objects.filter(owner=request.user)
    context = {
        'expenses':expenses
    }
    return render(request, 'expenses/index.html', context)

def add_despesa(request):
    categories = Category.objects.all()
    context  = {
        'categories':categories,
        'values': request.POST
    }
    
    if request.method == 'POST':
        
        amount = request.POST['amount']
        if not amount:
            messages.error(request, 'Quantidade é requerida')
            return render(request, 'expenses/add_despesas.html', context)
        
        descricao = request.POST['descricao']
        date = request.POST['expense_date']
        category = request.POST['category']
        
        if not descricao:
            messages.error(request, 'Uma descrição é requerida')
            return render(request, 'expenses/add_despesas.html', context)
        Expense.objects.create(
            owner=request.user,
            amount = amount,
            description=descricao,
            date=date,
            category=category
        )
        messages.success(request, 'Despesa salva com sucesso.')
        return redirect('despesas')
    return render(request, 'expenses/add_despesas.html', context)

def despesa_editar(request, id):
    expense = Expense.objects.get(pk=id)
    categories = Category.objects.all()
    context = {
        'expense': expense,
        'values':expense,
        'categories':categories,
    }
    if request.method == 'GET':
        return render(request,'expenses/edit-expense.html', context)
    if request.method == 'POST':
        amount = request.POST['amount']
        if not amount:
            messages.error(request, 'Quantidade é requerida')
            return render(request, 'expenses/edit-expense.html', context)
        
        descricao = request.POST['descricao']
        date = request.POST['expense_date']
        category = request.POST['category']
        
        if not descricao:
            messages.error(request, 'Uma descrição é requerida')
            return render(request, 'expenses/edit-expense.html', context)
        
        expense.owner=request.user
        expense.amount = amount
        expense.description=descricao
        expense.date=date
        expense.category=category
        
        expense.save()
        messages.info(request,'Despesa atualizada com sucesso')
        return redirect('despesas')

        
def deletar_despesa(request, id):
    expense = Expense.objects.get(pk=id)
    expense.delete()
    messages.success(request, 'Despesa Deletada.')
    return redirect('despesas')