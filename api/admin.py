from django.contrib import admin
from api.models import Specialization, Procedure, Visit, Patient, Doctor

admin.site.register(Specialization)
admin.site.register(Procedure)
admin.site.register(Visit)
admin.site.register(Patient)
admin.site.register(Doctor)
