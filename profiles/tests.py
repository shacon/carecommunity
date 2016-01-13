from django.test import TestCase
from django.test import TestCase, Client
from caretaker.models import Caregiver
from django.core.urlresolvers import reverse
from django_test_mixins import FormValidationTestCase, HttpCodeTestCase



class TestProfileList(TestCase):
    def test_search_renders(self):
        response = self.client.get(reverse('search'))
        self.assertEqual(response.status_code, 200)

# Create your tests here.
