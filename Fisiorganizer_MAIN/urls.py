from django.urls import re_path, include
from django.contrib import admin

urlpatterns = [
    re_path(r'^admin/', admin.site.urls),
    re_path(r'^', include('Fisiorganizer_SITE.urls')),
    re_path(r'^rest/', include('Fisiorganizer_API.urls'))
]
