from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from Fisiorganizer_SITE.forms import EvolutionForm
from Fisiorganizer_SITE.controllers import evolution_controller


@login_required
def create(request):
    evolution_form = EvolutionForm(request)

    if request.method == "POST":
        form = EvolutionForm(request.POST)
        if form.is_valid():

            # TODO: map form to model

            print("object saved")
            return redirect(evolution_controller.list)
        else:
            print(form.errors)
    else:
        return render(request, "evolution/evolution_create.html", {'evolutionForm': evolution_form})


def edit(request):
    return HttpResponse("editar")


def delete(request):
    return HttpResponse("excluir")


def details(request):
    return HttpResponse("ver")


def list(request):
    return HttpResponse("listar")