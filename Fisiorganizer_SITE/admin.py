from django.contrib import admin
from Fisiorganizer_SITE.models import UserExtra, Session, Patient, Modality, Service

# Register your models here.
admin.site.register(UserExtra)
admin.site.register(Session)
admin.site.register(Patient)
admin.site.register(Modality)
admin.site.register(Service)

