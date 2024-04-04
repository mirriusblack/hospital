from django.contrib import admin
from api.models import Specialization, Procedure, Visit, Patient, Doctor, Schedule, Department, Finance

admin.site.register(Specialization)
admin.site.register(Procedure)
admin.site.register(Visit)
admin.site.register(Patient)
admin.site.register(Doctor)
admin.site.register(Schedule)
admin.site.register(Department)
admin.site.register(Finance)