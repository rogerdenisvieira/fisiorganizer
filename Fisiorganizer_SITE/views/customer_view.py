from django.shortcuts import render
from django.http import HttpResponse


def create(request):
    return HttpResponse("criar aluno")

def edit(request):
    return HttpResponse("editar aluno")

def delete(request):
    return HttpResponse("excluir aluno")

def show(request):
    return HttpResponse("ver")


