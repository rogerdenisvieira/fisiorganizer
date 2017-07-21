from django.conf import settings
from django.conf.urls import url, include
from django.views.static import serve
from django.conf.urls import handler404
from Fisiorganizer_SITE.controllers import main_controller, customer_controller, session_controller, account_controller, exercise_controller



# route for customers
customer_patterns = [
    url(r'^edit/(?P<id>[0-9]{1})', customer_controller.edit, name='customer_edit'),
    url(r'^delete', customer_controller.delete, name='customer_delete'),
    url(r'^create', customer_controller.create, name='customer_create'),
    url(r'^details/(?P<id>[0-9]{1})', customer_controller.details, name='customer_details'),
    url(r'^list', customer_controller.list, name='customer_list')
]

# routes for sessions
session_patterns = [
    url(r'^edit/(?P<id>[0-9]{1})', session_controller.edit, name='session_edit'),
    url(r'^delete', session_controller.delete, name='session_delete'),
    url(r'^create', session_controller.create, name='session_create'),
    url(r'^details/(?P<id>[0-9]{1})', session_controller.details, name='session_details'),
    url(r'^list', session_controller.list, name='session_list')
]

# routes for exercises
exercise_patterns = [
    url(r'^edit', exercise_controller.edit, name='exercise_edit'),
    url(r'^delete', exercise_controller.delete, name='exercise_delete'),
    url(r'^create', exercise_controller.create, name='exercise_create'),
    url(r'^details', exercise_controller.details, name='exercise_details'),
    url(r'^list', exercise_controller.list, name='exercise_list')
]

# routes used for authentication
authentication_patterns = [
    url(r'^login', account_controller.login_user, name='account_login'),
    url(r'^logout', account_controller.logout_user, name='logout_user')
]


urlpatterns = [
    url(r'^$', main_controller.index, name='index'),
    url(r'^customer/',include(customer_patterns)),
    url(r'^session/',include(session_patterns)),
    url(r'^exercise/',include(exercise_patterns)),
    url(r'^account/',include(authentication_patterns))
]

handler404 = 'Fisiorganizer_SITE.controllers.main_controler.pageNotFound'