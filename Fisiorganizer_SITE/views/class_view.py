from django.shortcuts import render
from django.http import HttpResponse


def create(request):
    return HttpResponse("criar aula")

def edit(request):
    return HttpResponse("editar aula")

def delete(request):
    return HttpResponse("excluir aula")

def show(request):
    return HttpResponse("ver aula")


