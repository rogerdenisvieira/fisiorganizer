from django.shortcuts import render

import datetime
from django.http import HttpResponse
from django.contrib.auth.models import User
from Fisiorganizer_SITE.models import Session



def index(request):

    # TODO: refatorar esse monstro
    user = request.user
    today = datetime.date.today()
    sessions = Session.objects.filter(id_instructor=user | date=today)
    
    
    



    days = ["Segunda-feira", "Terça-feira", "Quarta-feira", "Quinta-feira", "Sexta-feira", "Sábado", "Domingo"]
    dayNumber = today.weekday()
    dayOfWeek = days[dayNumber]

    return render(request, 'index.html', {'dayOfWeek': dayOfWeek, 'sessions': sessions})



