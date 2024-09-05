
from django.views.generic import CreateView, DetailView, ListView, UpdateView   
from Fisiorganizer_SITE.forms import EvolutionForm
from Fisiorganizer_SITE.models import Evolution


class EvolutionCreateView(CreateView):
    model = Evolution
    form_class = EvolutionForm
    template_name = 'evolution/evolution_create.html'
    success_url = '/'

class EvolutionDetailView(DetailView):
    model = Evolution
    template_name = 'evolution/evolution_detail.html'
    
class EvolutionListView(ListView):
    model = Evolution
    template_name = 'evolution/evolution_list.html'

class EvolutionUpdateView(UpdateView):
    model = Evolution
    form_class = EvolutionForm
  