from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='despesas'),
    path('add-despesa', views.add_despesa, name='add-despesa'),
    path('despesa-editar/<id>', views.despesa_editar, name='despesa-editar'),
    path('despesa-deletar/<id>', views.deletar_despesa, name='deletar-despesa')
]
