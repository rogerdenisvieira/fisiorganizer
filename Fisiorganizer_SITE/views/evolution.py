from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.core.paginator import Paginator
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
            evolution_model: Evolution = evolution_form.save(commit=False)
            evolution_model.customer = request.POST['id_customer']
            evolution_model.date = request.POST['date']
            evolution_model.evolution_text = request.POST['evolution_text']
            evolution_model.save()
            
            
            logging.info("saving evolution into db") 

            return redirect(list)
        else:
            print(evolution_form.errors)
    else:
        evolution_form = EvolutionForm()
        return render(request, "evolution/evolution_create.html", {'evolutionForm': evolution_form})


def edit(request):
    return HttpResponse("editar")


def delete(request):
    return HttpResponse("excluir")

@login_required
def details(request, id):
    evolution = get_object_or_404(Evolution, id=id)

    dto = {
        'id': evolution.id,
        'Paciente': evolution.id_customer,
        'Data': evolution.date,
        'Descrição': evolution.evolution_text,
    }

    return render(request, 'evolution/evolution_details.html', {'dto': dto.items})

@login_required
def list(request):
    evolution_list = Evolution.objects.all()
    paginator = Paginator(evolution_list, 10)  # Show 10 evolutions per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'evolution/evolution_list.html', {'page_obj': page_obj})