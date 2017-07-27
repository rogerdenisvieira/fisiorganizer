from django.shortcuts import render
import datetime
from django.http import HttpResponse
from django.contrib.auth.models import User
from Fisiorganizer_SITE.models import Session
from Fisiorganizer_SITE.helpers import date_helper


def index(request):
    dayOfWeek = date_helper.getDayOfWeek

    # if user is authenticated, returns his sessions, else, returns just the page
    if request.user.is_authenticated():
        today = datetime.date.today()
        user = request.user
        sessions = Session.objects.filter(date=today, id_instructor=user)
        return render(request, 'index.html', {'dayOfWeek': dayOfWeek, 'sessions': sessions})
    else:
        return render(request, 'index.html')

def pageNotFound(request):
    return render(request, '404.html')





