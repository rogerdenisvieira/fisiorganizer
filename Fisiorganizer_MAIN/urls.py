from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include('Fisiorganizer_SITE.urls')),
    url(r'^rest/', include('Fisiorganizer_API.urls'))
]
