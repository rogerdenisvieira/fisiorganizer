from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from Fisiorganizer_SITE.forms import SessionForm
from Fisiorganizer_SITE.controllers import session_controller
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
            return redirect(session_controller.list)
        else:
            print(session_form.errors)
    else:
        session_form = SessionForm()
        return render(request, 'session/session_create.html', {'sessionForm': session_form})


def edit(request):
    return HttpResponse("editar aula")


def delete(request):
    return HttpResponse("excluir aula")


def details(request, id):
    return HttpResponse("ver aula")


def list(request):
    sessions = Session.objects.all()
    return render(request, 'session/session_list.html', {'sessions': sessions})
