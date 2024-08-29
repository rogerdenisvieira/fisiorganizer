from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from Fisiorganizer_SITE.forms import SessionForm
from Fisiorganizer_SITE.views import session_view
from Fisiorganizer_SITE.models import Session


@login_required
def create(request):
    if request.method == 'POST':
        session_form = SessionForm(request.POST)
        if session_form.is_valid():
            session = session_form.save(commit=False)
            session.instructor = request.POST['id_instructor']
            session.customer = request.POST['id_customer']
            session.date = request.POST['date']
            session.time = request.POST['time']
            session.save()

            print('saving session into db')
            return redirect(session_view.list)
        else:
            print(session_form.errors)
    else:
        session_form = SessionForm()
        return render(request, 'session/session_create.html', {'sessionForm': session_form})


def edit(request, id):
    return HttpResponse("editar aula")


def delete(request):
    return HttpResponse("excluir aula")


def details(request, id):
    session = get_object_or_404(Session, id=id)
    exercises = Exercise.objects.all()


    sessionDTO = {
        'Instrutor': session.id_instructor.username,
        'Aluno': session.id_customer.name,
        'Data': session.date,
        'Hora': session.time
    }

    return render(request, 'session/session_details.html', {'sessionDTO': sessionDTO.items()})


def list(request):
    sessions = Session.objects.all()
    return render(request, 'session/session_list.html', {'sessions': sessions})
