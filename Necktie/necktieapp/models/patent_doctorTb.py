from django.db import models

from .doctors import Doctors
from .patients import Patient


class PatentDoctorTb(models.Model):
    '''
    we can add extra fields here
    '''

    doctor = models.ForeignKey(Doctors, blank=False, null=False, on_delete=models.CASCADE)
    patient = models.ForeignKey(Patient, blank=False, null=False, on_delete=models.CASCADE)
