from django.conf import settings
from django.conf.urls import url
from django.views.static import serve
from Fisiorganizer_SITE.views import main_view, customer_view, session_view, account_view, exercise_view


urlpatterns = [
    url(r'^$', main_view.index, name='index'),

    # route for customers
    url(r'^customer/edit/(?P<id>[0-9]{1})', customer_view.edit, name='customer_edit'),
    url(r'^customer/delete', customer_view.delete, name='customer_delete'),
    url(r'^customer/create', customer_view.create, name='customer_create'),
    url(r'^customer/details/(?P<id>[0-9]{1})', customer_view.details, name='customer_details'),
    url(r'^customer/list', customer_view.list, name='customer_list'),

    # routes for sessions
    url(r'^session/edit', session_view.edit, name='session_edit'),
    url(r'^session/delete', session_view.delete, name='session_delete'),
    url(r'^session/create', session_view.create, name='session_create'),
    url(r'^session/details', session_view.details, name='session_details'),
    url(r'^session/list', session_view.list, name='session_list'),

    # routes for exercises
    url(r'^exercise/edit', exercise_view.edit, name='exercise_edit'),
    url(r'^exercise/delete', exercise_view.delete, name='exercise_delete'),
    url(r'^exercise/create', exercise_view.create, name='exercise_create'),
    url(r'^exercise/details', exercise_view.details, name='exercise_details'),
    url(r'^exercise/list', exercise_view.list, name='exercise_list'),

    # routes used for authentication
    url(r'^account/login', account_view.login_user, name='account_login'),
    url(r'^account/logout', account_view.logout_user, name='logout_user')








]
