from Fisiorganizer_SITE.forms import PlaceForm
from Fisiorganizer_SITE.models import Place
from django.views.generic import CreateView, ListView, DetailView, DeleteView


class PlaceCreateView(CreateView):
    model = Place
    form_class = PlaceForm
    success_url = '/place/list/'
    template_name = 'place/place_create.html'

class PlaceDetailView(DetailView):
    model = Place
    template_name = 'place/place_detail.html'

class PlaceListView(ListView):
    model = Place
    template_name = 'place/place_list.html'

class PlaceDeleteView(DeleteView):
    model = Place
    template_name = 'place/place_delete.html'
    success_url = '/place/list/'