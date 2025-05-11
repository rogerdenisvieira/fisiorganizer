from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.views.generic import ListView
from django.contrib.auth.decorators import login_required
from Fisiorganizer_SITE.forms import EvolutionForm
from Fisiorganizer_SITE.views import evolution
from Fisiorganizer_SITE.models import Evolution
import logging
from logging import basicConfig


@login_required
def create(request):
    if request.method == "POST":
        evolution_form = EvolutionForm(request.POST)
        if evolution_form.is_valid():
            evolution: Evolution = evolution_form.save(commit=False)
            evolution.customer = request.POST['id_customer']
            evolution.date = request.POST['date']
            evolution.evolution_text = request.POST['evolution_text']
            evolution.save()
            
            
            logging.info("saving evolution into db")

            return redirect(evolution.list)
        else:
            print(evolution_form.errors)
    else:
        evolution_form = EvolutionForm()
        return render(request, "evolution/evolution_create.html", {'evolutionForm': evolution_form})


def edit(request):
    return HttpResponse("editar")


def delete(request):
    return HttpResponse("excluir")


def details(request):
    return HttpResponse("ver")


def list(request):
    return HttpResponse("listar")


class EvolutionList(ListView):
    model = Evolution