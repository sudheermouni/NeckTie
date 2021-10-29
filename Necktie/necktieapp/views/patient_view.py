from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, filters
from rest_framework.permissions import IsAuthenticated
from necktieapp.models import Patient
from necktieapp.serializers import PatientSerializer


class PatientViewset(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)

    queryset = Patient.objects.all()
    serializer_class = PatientSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['id', 'p_surname', 'p_username']
    search_fields = ['id', 'p_surname', 'p_username']
    ordering_fields = ['id', 'p_surname', 'p_username']
