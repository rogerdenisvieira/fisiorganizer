from django.conf import settings
from django.urls import re_path, include
from django.views.static import serve
from django.conf.urls import handler404
from Fisiorganizer_SITE.views import account_view, customer_view, evolution_view, main_view, session_view

# route for customers
customer_patterns = [
    re_path(r'^edit/(?P<id>[0-9]{1})', customer_view.edit, name='customer_edit'),
    re_path(r'^delete', customer_view.delete, name='customer_delete'),
    re_path(r'^create', customer_view.create, name='customer_create'),
    re_path(r'^details/(?P<id>[0-9]{1})', customer_view.details, name='customer_details'),
    re_path(r'^list', customer_view.list, name='customer_list')
]

# routes for sessions
session_patterns = [
    re_path(r'^edit/(?P<id>[0-9]{1})', session_view.edit, name='session_edit'),
    re_path(r'^delete', session_view.delete, name='session_delete'),
    re_path(r'^create', session_view.create, name='session_create'),
    re_path(r'^details/(?P<id>[0-9]{1})', session_view.details, name='session_details'),
    re_path(r'^list', session_view.list, name='session_list')
]

# routes used for authentication
authentication_patterns = [
    re_path(r'^login', account_view.login_user, name='account_login'),
    re_path(r'^logout', account_view.logout_user, name='logout_user')
]

evolution_patterns = [
    re_path(r'^edit/(?P<id>[0-9]{1})', evolution_view.edit, name='evolution_edit'),
    re_path(r'^delete', evolution_view.delete, name='evolution_delete'),
    re_path(r'^create', evolution_view.create, name='evolution_create'),
    re_path(r'^details/(?P<id>[0-9]{1})', evolution_view.details, name='evolution_details'),
    re_path(r'^list', evolution_view.list, name='evolution_list')
]

urlpatterns = [
    re_path(r'^$', main_view.index, name='index'),
    re_path(r'^customer/',include(customer_patterns)),
    re_path(r'^session/',include(session_patterns)),
    re_path(r'^account/',include(authentication_patterns))
]

handler404 = 'Fisiorganizer_SITE.controllers.main_controller.pageNotFound'