from django.contrib import admin
from Fisiorganizer_SITE.models import UserExtra, Session, Patient, Modality, Level

# Register your models here.
admin.site.register(UserExtra)
admin.site.register(Session)
admin.site.register(Patient)
admin.site.register(Modality)
admin.site.register(Level)

