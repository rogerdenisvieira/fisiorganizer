from django.conf import settings
from django.conf.urls import url
from django.views.static import serve
from Fisiorganizer_SITE.views import main_view, customer_view, session_view, account_view
from Fisiorganizer_SITE.views.session_view import SessionCreate


urlpatterns = [
    url(r'^$', main_view.index, name='index'),

    #rotas para os alunos
    url(r'^customer/edit', customer_view.edit, name='customer_edit'),
    url(r'^customer/delete', customer_view.delete, name='customer_delete'),
    url(r'^customer/create', customer_view.create, name='customer_create'),
    url(r'^customer/view', customer_view.show, name='customer_show'),

    #rotas para as aulas
    url(r'^session/create/$', SessionCreate.as_view(), name='session_create'),


    #rotas para autenticação
    url(r'^account/login', account_view.login_user, name='account_login')




]
