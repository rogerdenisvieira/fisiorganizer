from django.conf import settings
from django.urls import re_path, include
from django.views.static import serve
from django.conf.urls import handler404
from Fisiorganizer_SITE.controllers import main_controller, customer_controller, session_controller, account_controller, exercise_controller



# route for customers
customer_patterns = [
    re_path(r'^edit/(?P<id>[0-9]{1})', customer_controller.edit, name='customer_edit'),
    re_path(r'^delete', customer_controller.delete, name='customer_delete'),
    re_path(r'^create', customer_controller.create, name='customer_create'),
    re_path(r'^details/(?P<id>[0-9]{1})', customer_controller.details, name='customer_details'),
    re_path(r'^list', customer_controller.list, name='customer_list')
]

# routes for sessions
session_patterns = [
    re_path(r'^edit/(?P<id>[0-9]{1})', session_controller.edit, name='session_edit'),
    re_path(r'^delete', session_controller.delete, name='session_delete'),
    re_path(r'^create', session_controller.create, name='session_create'),
    re_path(r'^details/(?P<id>[0-9]{1})', session_controller.details, name='session_details'),
    re_path(r'^list', session_controller.list, name='session_list'),
    re_path(r'^/(?P<id>[0-9]{1})/exercise/add', session_controller.add_exercise, name="add_session_exercise")
]

# routes for exercises
exercise_patterns = [
    re_path(r'^edit', exercise_controller.edit, name='exercise_edit'),
    re_path(r'^delete', exercise_controller.delete, name='exercise_delete'),
    re_path(r'^create', exercise_controller.create, name='exercise_create'),
    re_path(r'^details', exercise_controller.details, name='exercise_details'),
    re_path(r'^list', exercise_controller.list, name='exercise_list')
]

# routes used for authentication
authentication_patterns = [
    re_path(r'^login', account_controller.login_user, name='account_login'),
    re_path(r'^logout', account_controller.logout_user, name='logout_user')
]


urlpatterns = [
    re_path(r'^$', main_controller.index, name='index'),
    re_path(r'^customer/',include(customer_patterns)),
    re_path(r'^session/',include(session_patterns)),
    re_path(r'^exercise/',include(exercise_patterns)),
    re_path(r'^account/',include(authentication_patterns))
]

handler404 = 'Fisiorganizer_SITE.controllers.main_controller.pageNotFound'