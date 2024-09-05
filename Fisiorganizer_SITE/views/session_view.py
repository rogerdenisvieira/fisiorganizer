from django.views.generic import CreateView, DetailView, ListView, DeleteView, UpdateView
from Fisiorganizer_SITE.forms import SessionForm
from Fisiorganizer_SITE.models import Session

class SessionCreateView(CreateView):
    model = Session
    form_class = SessionForm
    template_name = 'session/session_create.html'
    success_url = '/'

class SessionDetailView(DetailView):
    model = Session
    template_name = 'session/session_detail.html'

class SessionListView(ListView):
    model = Session
    template_name = 'session/session_list.html'

class SessionDeleteView(DeleteView):
    model = Session
    template_name = 'session/session_delete.html'
    success_url = '/session/list'

class SessionUpdateView(UpdateView):
    model = Session
    form_class = SessionForm
    template_name = 'session/session_edit.html'
    success_url = '/session/list'
