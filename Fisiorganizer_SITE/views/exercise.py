from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from Fisiorganizer_SITE.forms import ExerciseForm

@login_required
def create(request):
    exercise_form = ExerciseForm()

    if request.method == 'POST':
        # TODO implement persistence of customer
        print('it was a post')
    else:
        return render(request, 'exercise/exercise_create.html', {'exerciseForm': exercise_form})

def edit(request):
    return HttpResponse("editar")


def delete(request):
    return HttpResponse("excluir")


def details(request):
    return HttpResponse("ver")


def list(request):
    return HttpResponse("listar")