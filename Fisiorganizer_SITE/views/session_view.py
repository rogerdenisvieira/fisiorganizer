from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from Fisiorganizer_SITE.models import Session
from django.views.generic.edit import CreateView, UpdateView, DeleteView


login_required
class SessionCreate(CreateView):
    model = Session
    fields = ['id_instructor']



