from django.conf import settings
from django.conf.urls import url
from django.views.static import serve
from Fisiorganizer_SITE.views import main_view, customer_view, class_view


urlpatterns = [
    url(r'^$', main_view.index, name='index'),

    #rotas para os alunos
    url(r'^customer/edit', customer_view.edit, name='customer_edit'),
    url(r'^customer/delete', customer_view.delete, name='customer_delete'),
    url(r'^customer/create', customer_view.create, name='customer_create'),
    url(r'^customer/view', customer_view.show, name='customer_show'),

    #rotas para as aulas
    url(r'^class/edit', class_view.edit, name='class_edit'),
    url(r'^class/delete', class_view.delete, name='class_delete'),
    url(r'^class/create', class_view.create, name='class_create'),
    url(r'^class/view', class_view.show, name='class_show')



]
