from django.contrib import admin
from .models import Doctors, Patient, PatentDoctorTb


admin.site.register(Doctors)
admin.site.register(Patient)
admin.site.register(PatentDoctorTb)
