from django.contrib import admin
from Fisiorganizer_SITE.models import UserExtra, Session, Exercise, Customer, Modality, Level, Equipment, Focus, ExerciseFocus, ExerciseEquipment, SessionExercise

# Register your models here.
admin.site.register(UserExtra)
admin.site.register(Session)
admin.site.register(Exercise)
admin.site.register(Customer)
admin.site.register(Modality)
admin.site.register(Level)
admin.site.register(Focus)
admin.site.register(Equipment)
admin.site.register(ExerciseEquipment)
admin.site.register(ExerciseFocus)
admin.site.register(SessionExercise)

