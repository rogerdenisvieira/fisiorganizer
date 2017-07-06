from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from Fisiorganizer_SITE.forms import SessionForm


@login_required
def create(request):
    session_form = SessionForm()

    if request.method == 'POST':
        # TODO implement persistence of customer
        print('it was a post')
    else:
        return render(request, 'session/session_create.html', {'sessionForm': session_form})


def edit(request):
    return HttpResponse("editar aula")


def delete(request):
    return HttpResponse("excluir aula")


def details(request):
    return HttpResponse("ver aula")


def list(request):
    return HttpResponse("listar aulas")
