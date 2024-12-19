from Fisiorganizer_SITE.forms import PatientForm
from Fisiorganizer_SITE.models import Patient
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView


class PatientCreateView(CreateView):
    model = Patient
    form_class = PatientForm
    template_name = 'patient/patient_create.html'
    success_url = '/patient/list/'

class PatientDetailView(DetailView):
    model = Patient
    template_name = 'patient/patient_detail.html'

class PatientListView(ListView):
    model = Patient
    template_name = 'patient/patient_list.html'

class PatientUpdateView(UpdateView):
    model = Patient
    form_class = PatientForm
    template_name = 'patient/patient_edit.html'
    success_url = '/patient/list/'

class PatientDeleteView(DeleteView):
    model = Patient
    template_name = 'patient/patient_delete.html'
    success_url = '/patient/list/'