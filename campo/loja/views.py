from django.shortcuts import render
from django.http import HttpResponse
from .models import Produto 
from django.db.models import Q  

def pesquisar(request):
    resultado = Produto.objects.filter(nome="Laranja")
    # print(resultado)
    # print("Opa Chegou aqui")
    return HttpResponse(resultado) 
