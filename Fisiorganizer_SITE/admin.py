from django.contrib import admin
from Fisiorganizer_SITE.models import User_extra, Session, Exercise, Customer, Trainning

# Register your models here.
admin.site.register(User_extra)
admin.site.register(Session)
admin.site.register(Exercise)
admin.site.register(Customer)
admin.site.register(Trainning)

