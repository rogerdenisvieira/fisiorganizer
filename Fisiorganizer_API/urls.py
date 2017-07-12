from django.conf import settings
from django.conf.urls import url
from django.views.static import serve
from Fisiorganizer_API.views import CustomerList


urlpatterns = [
    url(r'^customer/', CustomerList.as_view(), name='customer_list'),
    #url(r'^customer/(?P<id>[0-9]{1})', CustomerList.as_view(), name='customer_list'),
]