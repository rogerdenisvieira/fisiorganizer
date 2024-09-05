from django.conf import settings
from django.urls import re_path, include, path
from django.views.static import serve
from django.conf.urls import handler404
from Fisiorganizer_SITE.views import account_view, evolution_view, main_view, patient_view, session_view
from Fisiorganizer_SITE.views.place_view import PlaceCreateView, PlaceListView, PlaceDetailView, PlaceDeleteView
from Fisiorganizer_SITE.views.evolution_view import EvolutionCreateView, EvolutionDetailView, EvolutionListView
from Fisiorganizer_SITE.views.session_view import SessionCreateView, SessionDeleteView, SessionDetailView, SessionListView, SessionUpdateView
from Fisiorganizer_SITE.views.patient_view import PatientCreateView, PatientDeleteView, PatientDetailView, PatientListView, PatientUpdateView

# route for customers
patient_patterns = [
    path('create/', PatientCreateView.as_view(), name='patient_create'),
    path('detail/<pk>', PatientDetailView.as_view(), name='patient_detail'),
    path('list/', PatientListView.as_view(), name='patient_list'),
    path('edit/<pk>', PatientUpdateView.as_view(), name='patient_edit'),
    path('delete/<pk>', PatientDeleteView.as_view(), name='patient_delete')
]
# routes used for authentication
authentication_patterns = [
    re_path(r'^login', account_view.login_user, name='account_login'),
    re_path(r'^logout', account_view.logout_user, name='logout_user')
]

session_patterns = [   
    path('delete/<pk>', SessionDeleteView.as_view(), name='session_delete'),
    path('edit/<pk>', SessionUpdateView.as_view(), name='session_edit'),
    path('detail/<pk>', SessionDetailView.as_view(), name='session_detail'),
    path('list/', SessionListView.as_view(), name='session_list'),
    path('create/', SessionCreateView.as_view(), name='session_create')
]

evolution_patterns = [
    path(r'create/', EvolutionCreateView.as_view(), name='evolution_create'),
    path(r'detail/<pk>', EvolutionDetailView.as_view(), name='evolution_detail'),
    path(r'list/', EvolutionListView.as_view(), name='evolution_list'),
    path(r'edit/<pk>', evolution_view.EvolutionUpdateView.as_view(), name='evolution_edit')
]

place_patterns = [
    path('create/', PlaceCreateView.as_view(), name='place_create'),
    path('detail/<pk>', PlaceDetailView.as_view(), name='place_detail'),
    path('list/', PlaceListView.as_view(), name='place_list'),
    path('delete/<pk>', PlaceDeleteView.as_view(), name='place_delete')
]

urlpatterns = [
    re_path(r'^$', main_view.index, name='index'),
    re_path(r'^patient/',include(patient_patterns)),
    re_path(r'^session/',include(session_patterns)),
    re_path(r'^account/',include(authentication_patterns)),
    re_path(r'^evolution/',include(evolution_patterns)),
    re_path(r'^place/', include(place_patterns)),
]

handler404 = 'Fisiorganizer_SITE.controllers.main_view.pageNotFound'