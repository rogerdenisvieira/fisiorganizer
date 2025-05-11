from django.conf import settings
from django.urls import re_path, include
from django.views.static import serve
from django.conf.urls import handler404
from Fisiorganizer_SITE.views import account, customer, evolution, exercise, main, session
from Fisiorganizer_SITE.views.accounting import entry



# route for customers
customer_patterns = [
    re_path(r'^edit/(?P<id>\d{1,})', customer.edit, name='customer_edit'),
    re_path(r'^delete', customer.delete, name='customer_delete'),
    re_path(r'^create', customer.create, name='customer_create'),
    re_path(r'^details/(?P<id>\d{1,})', customer.details, name='customer_details'),
    re_path(r'^list', customer.list, name='customer_list')
]

evolution_patterns = [
    re_path(r'create', evolution.create, name="evolution_create"),
    re_path(r'list', evolution.list, name="evolution_list"),
    re_path(r'^edit/(?P<id>\d{1,})', evolution.edit, name='evolution_edit'),
    re_path(r'delete', evolution.delete, name="evolution_delete"),
    re_path(r'^details/(?P<id>\d{1,})', evolution.details, name='evolution_details')
]

# routes for sessions
session_patterns = [
    re_path(r'^edit/(?P<id>[0-9]{1})', session.edit, name='session_edit'),
    re_path(r'^delete', session.delete, name='session_delete'),
    re_path(r'^create', session.create, name='session_create'),
    re_path(r'^details/(?P<id>[0-9]{1})', session.details, name='session_details'),
    re_path(r'^list', session.list, name='session_list'),
    re_path(r'^/(?P<id>[0-9]{1})/exercise/add', session.add_exercise, name="add_session_exercise"),
    re_path(r'^(?P<id>\d{1,})/exercise/delete', session.delete_exercise, name="delete_session_exercise")
]

# routes for exercises
exercise_patterns = [
    re_path(r'^edit', exercise.edit, name='exercise_edit'),
    re_path(r'^delete', exercise.delete, name='exercise_delete'),
    re_path(r'^create', exercise.create, name='exercise_create'),
    re_path(r'^details', exercise.details, name='exercise_details'),
    re_path(r'^list', exercise.list, name='exercise_list')
]

accounting_entry_patterns = [
    re_path(r'^edit', entry.edit, name='accounting_edit'),
    re_path(r'^delete', entry.delete, name='accounting_delete'),
    re_path(r'^create', entry.create, name='accounting_create'),
    re_path(r'^details', entry.details, name='accounting_details'),
    re_path(r'^list', entry.list, name='accounting_list')
]

# routes used for authentication
authentication_patterns = [
    re_path(r'^login', account.login_user, name='account_login'),
    re_path(r'^logout', account.logout_user, name='logout_user')
]

# build all URLs together
urlpatterns = [
    re_path(r'^$', main.index, name='index'),
    re_path(r'^customer/',include(customer_patterns)),
    re_path(r'^session/',include(session_patterns)),
    re_path(r'^exercise/',include(exercise_patterns)),
    re_path(r'^account/',include(authentication_patterns)),
    re_path(r'^evolution/',include(evolution_patterns)),
    re_path(r'^accounting/entry/',include(accounting_entry_patterns))
]

handler404 = 'Fisiorganizer_SITE.views.main.pageNotFound'