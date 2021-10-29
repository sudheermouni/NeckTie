from rest_framework import serializers
from necktieapp.models import Doctors

class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctors
        fields = "__all__"