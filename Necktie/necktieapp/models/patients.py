from django.db import models

from .doctors import Doctors


class Patient(models.Model):
    p_surname = models.CharField(max_length=20, blank=True, null=True)
    doctor = models.ManyToManyField(Doctors, through="PatentDoctorTb", null=True, blank=True)
    p_fullname = models.CharField(max_length=20, blank=True, null=True)
    p_username = models.CharField(max_length=40, blank=False, null=False)
    p_phone = models.CharField(max_length=10, blank=True, null=True)
    p_country = models.CharField(max_length=50, blank=True, null=True)
    p_state = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return self.p_username