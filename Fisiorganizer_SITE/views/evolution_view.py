
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from Fisiorganizer_SITE.forms import EvolutionForm


@login_required
def create(request):
    if request.method == 'POST':
        session_form = EvolutionForm(request.POST)
        if session_form.is_valid():

            print('saving session into db')
            return redirect(evolution_view.list)
        else:
            print(session_form.errors)
    else:
        EvolutionForm = EvolutionForm()
        return render(request, 'evolution/evolution_create.html', {'evolutionForm': evolution_form})

def edit(request, id):
    return HttpResponse("editar aula")


def delete(request):
    return HttpResponse("excluir aula")


def details(request, id):
    pass


def list(request):
    pass