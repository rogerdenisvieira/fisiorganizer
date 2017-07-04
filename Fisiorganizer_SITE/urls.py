from django.conf import settings
from django.conf.urls import url
from django.views.static import serve
from Fisiorganizer_SITE.views import main_view, customer_view, session_view


urlpatterns = [
    url(r'^$', main_view.index, name='index'),

    #rotas para os alunos
    url(r'^customer/edit', customer_view.edit, name='customer_edit'),
    url(r'^customer/delete', customer_view.delete, name='customer_delete'),
    url(r'^customer/create', customer_view.create, name='customer_create'),
    url(r'^customer/view', customer_view.show, name='customer_show'),

    #rotas para as aulas
    url(r'^session/edit', session_view.edit, name='session_edit'),
    url(r'^session/delete', session_view.delete, name='session_delete'),
    url(r'^session/create', session_view.create, name='session_create'),
    url(r'^session/view', session_view.show, name='session_show')



]
