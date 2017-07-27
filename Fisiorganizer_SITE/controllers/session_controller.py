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
    session_exercises = SessionExercise.objects.filter(id_session=id)
    exercises_dto = []
    session_exercises_dto = []

    # information about the session
    session_dto = {
        'Instrutor': session.id_instructor.username,
        'Aluno': session.id_customer.name,
        'Data': session.date,
        'Hora': session.time,
    }

    # to list exercises in current session
    for session_exercise in session_exercises:
        session_exercise_dto = {
            'id': session_exercise.id,
            'exercise_name': session_exercise.id_exercise.name,
            'level': session_exercise.id_exercise.id_level.name,
            'id_exercise': session_exercise.id_exercise.id
        }
        session_exercises_dto.append(session_exercise_dto)

    # to populate dropdown with exercises
    for exercise in exercises:
        exercise_dto = {
            'id': exercise.id,
            'name': exercise
        }
        exercises_dto.append(exercise_dto)

    return render(request, 'session/session_details.html', {'session_dto': session_dto.items(),
                                                            'session_exercises_dto': session_exercises_dto,
                                                            'exercises_dto': exercises_dto,
                                                            'session_id': id})


def list(request):
    sessions = Session.objects.all()
    return render(request, 'session/session_list.html', {'sessions': sessions})


def add_exercise(request, id):
    id_exercise=request.POST["id_exercise"]
    session = Session.objects.get(id=id)
    exercise = Exercise.objects.get(id=id_exercise)
    session_exercise = SessionExercise(id_session=session, id_exercise=exercise)
    session_exercise.save()
    return HttpResponse(status=200)


def delete_exercise(request,id): 
    id_exercise = request.POST["id_exercise"]
    id_session_exercise = request.POST["id_session_exercise"]    
    SessionExercise.objects.filter(id_exercise=id_exercise, 
                                   id_session=id, 
                                   id=id_session_exercise).delete()
    return HttpResponse(status=200)
