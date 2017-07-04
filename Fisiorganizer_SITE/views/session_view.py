from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse

@login_required
def create(request):
    return HttpResponse("criar aula")

def edit(request):
    return HttpResponse("editar aula")

def delete(request):
    return HttpResponse("excluir aula")

def show(request):
    return HttpResponse("ver aula")


