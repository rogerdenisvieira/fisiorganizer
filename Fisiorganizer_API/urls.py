from django.conf import settings
from django.conf.urls import url
from django.views.static import serve
from Fisiorganizer_API import views


urlpatterns = [
    url(r'^customer/(?P<id>[0-9]{1})', views.get_customer_by_id, name='customer_list'),
    url(r'^customer/$', views.get_all_customers, name='customer_list_all'),
]