import random
import string

from django.core.management.base import BaseCommand
from django.utils.crypto import get_random_string

from necktieapp.models import Doctors

sample_data = {
    'd_surname': get_random_string(),
    'd_firstname': get_random_string(),
    'd_username': "",
    'd_phone': get_random_string(),
    'd_address': get_random_string(),
    'd_country': get_random_string(),
    'd_specialization': "CD",
    'd_pincode': 524101,
}


class Command(BaseCommand):
    help = 'Create random doctors'

    def add_arguments(self, parser):
        parser.add_argument('total', type=int, help='Indicates the number of users to be created')

    def handle(self, *args, **kwargs):
        total = kwargs['total']
        list_instances = []
        Doctors.objects.all().delete()
        for i in range(total):
            sample_data['d_username'] = ''.join(random.choices(string.ascii_uppercase + string.digits, k=8))
            list_instances.append(Doctors(**sample_data))

        Doctors.objects.bulk_create(list_instances)
