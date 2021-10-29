from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, filters
from rest_framework.permissions import IsAuthenticated
from necktieapp.models import Doctors
from necktieapp.serializers import DoctorSerializer


class DoctorViewset(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)

    queryset = Doctors.objects.all()
    serializer_class = DoctorSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['id', 'd_specialization', 'd_username']
    search_fields = ['id', 'd_specialization', 'd_username']
    ordering_fields = ['id', 'd_specialization', 'd_username']
