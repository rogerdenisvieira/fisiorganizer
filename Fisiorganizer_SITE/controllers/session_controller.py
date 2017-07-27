from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from Fisiorganizer_SITE.forms import SessionForm
from Fisiorganizer_SITE.controllers import session_controller
from Fisiorganizer_SITE.models import Session, SessionExercise, Exercise


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


def edit(request, id):
    return HttpResponse("editar aula")

 
def delete(request):
    return HttpResponse("excluir aula")

# TODO refactor with snakecase 
def details(request, id):
    session = get_object_or_404(Session, id=id)
    exercises = Exercise.objects.all()
    sessionExercises = SessionExercise.objects.filter(id_session=id)
    exercisesDTO = []
    sessionExercisesDTO = []

    sessionDTO = {
        'Instrutor': session.id_instructor.username,
        'Aluno': session.id_customer.name,
        'Data': session.date,
        'Hora': session.time,
        'Id': session.id
    }

    # to list exercises in current session
    for sessionExercise in sessionExercises:
        sessionExerciseDTO = {
            'id': sessionExercise.id,
            'exercise_name': sessionExercise.id_exercise.name,
            'level': sessionExercise.id_exercise.id_level.name
        }
        sessionExercisesDTO.append(sessionExerciseDTO)

    # to populate dropdown with exercises
    for exercise in exercises:
        exerciseDTO = {
            'id': exercise.id,
            'content': exercise
        }
        exercisesDTO.append(exerciseDTO)

    return render(request, 'session/session_details.html', {'sessionDTO': sessionDTO.items(),
                                                            'sessionExercisesDTO': sessionExercisesDTO,
                                                            'exercisesDTO': exercisesDTO,
                                                            'session_id': id})


def list(request):
    sessions = Session.objects.all()
    return render(request, 'session/session_list.html', {'sessions': sessions})


def add_exercise(request, id):
    print('id da session de retorno' + id)
    print('id do exercício' + request.POST["id_exercise"])
    return HttpResponse('OK')


def delete_exercise(request):
    print('passei por aqui')
    pass
