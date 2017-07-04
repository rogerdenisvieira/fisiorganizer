from django.shortcuts import render
import datetime
from django.http import HttpResponse


def index(request):
    date = datetime.date.today()

    days = ["Segunda-feira", "Terça-feira", "Quarta-feira", "Quinta-feira", "Sexta-feira", "Sábado", "Domingo"]
    dayNumber = date.weekday()
    dayOfWeek = days[dayNumber]

    return render(request, 'index.html', {'dayOfWeek': dayOfWeek})



