from django.db import models
from model_utils import Choices

SPECIALIZATIONS = Choices(
    ("CD", "Cardiology"),
    ("GS", "General Surgery"),
    ("EC", "Endocrinology"),
    ("NT", "Neonatology"),
)


class Doctors(models.Model):
    d_surname = models.CharField(max_length=20, blank=True, null=True)
    d_firstname = models.CharField(max_length=20, blank=True, null=True)
    d_username = models.CharField(max_length=40, blank=False, null=False, unique=True)
    d_phone = models.CharField(max_length=10, blank=True, null=True)
    d_address = models.TextField(blank=True, null=True)
    d_country = models.CharField(max_length=30)
    d_specialization = models.CharField(
        choices=SPECIALIZATIONS,
        max_length=4,
        blank=False,
        null=False,
    )
    d_pincode = models.IntegerField()

    def __str__(self):
        return self.d_username
