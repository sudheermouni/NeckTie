from django.test import TestCase, TransactionTestCase
from necktieapp.models import Doctors

sample_data = {
    'd_surname': "sudheer",
    'd_firstname': "mandi",
    'd_username': "smre",
    'd_phone': "7702231789",
    'd_address': "Ramalingapuram",
    'd_country': "India",
    'd_specialization': "CD",
    'd_pincode': 524101,
}


class TestDoctor(TransactionTestCase):
    fixtures = ["doctors.json"]

    def test_create_new_record(self):
        model_instance = Doctors.objects.create(**sample_data)
        self.assertIsInstance(model_instance, Doctors)
        self.assertEqual(model_instance.d_username, "smre")

    def test_update_record(self):
        instance = Doctors.objects.get(id=1)
        instance.d_phone = "9177935906"
        instance.save()
        self.assertEqual(instance.d_phone, "9177935906")

    def test_should_not_save_duplicate_username(self):
        before_count = Doctors.objects.count()
        sample_data["d_username"] = "smreddy"
        try:
            Doctors.objects.create(**sample_data)
        except Exception as e:
            after_count = Doctors.objects.count()
            self.assertEqual(before_count, after_count)

