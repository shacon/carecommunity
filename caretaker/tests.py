from django.test import TestCase, Client
from .models import Caregiver
from django.core.urlresolvers import reverse
from django.contrib.auth import authenticate, login 
from django_test_mixins import FormValidationTestCase, HttpCodeTestCase
from .forms import Signup

class TestIndex(TestCase):
    def test_index_renders(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)

class TestSignup(HttpCodeTestCase, FormValidationTestCase):

    def form_params(self):
        return {'first_name': 'jessica',
                'last_name': 'jones',
                'email': 'jess@jones.com',
                'password': 'helloworld1'}

    def test_signupview_renders(self):
        response = self.client.get(reverse('signup'))
        self.assertHttpOK(response)

    def test_user_created(self):
        params = self.form_params()
        expected_email = params['email']
        response = self.client.post(
            reverse('signup'), self.form_params())
        self.assertTrue(
            Caregiver.objects.filter(email=expected_email).exists()
            )

    def test_password_required(self):
        params = self.form_params()
        params.pop('password')

        response = self.client.post(
            reverse('signup'), params)
        self.assertFormInvalid(response)

    def test_email_required(self):
        params = self.form_params()
        params.pop('email')

        response = self.client.post(
            reverse('signup'), params)
        self.assertFormInvalid(response)


class TestLogin(HttpCodeTestCase, FormValidationTestCase):
    def form_params(self):
        return {'email': 'jess@jones.com',
                'password': 'helloworld1'}

    def test_loginview_renders(self):
	response = self.client.get(reverse('login'))
	self.assertHttpOK(response)

    def test_user_loggedin(self):

    	user = Caregiver.objects.create_user(email='jess@jones.com', first_name='jess', last_name='jones', password='password')
        params = self.form_params()
	expected_email = params['email']
	response = self.client.post(
        reverse('login'), self.form_params())

        self.assertTrue(
            Caregiver.objects.filter(email=expected_email).exists()
            )
        # response = self.client.get(reverse('another-page-which-requires-authentication'))

    
class TestLogout(HttpCodeTestCase, FormValidationTestCase):
         
        def login_user(self):
	    user_email = 'jess@jones.com'
	    user_password = 'password'
            user = Caregiver.objects.create_user(email=user_email, first_name='jess', last_name='jones', password=user_password)
	    user = authenticate(email=user_email, password=user_password)
            self.client.login(email=user_email,
                          password=user_password)


	def test_logoutview_renders(self):
	    self.login_user()
	    response = self.client.get(reverse('logout'))
	    self.assertHttpOK(response)


class TestModels(TestCase):

	def test_caretaker(self):
	    email = 'jessica@jones.com'
	    first_name = 'jessica'
            last_name = 'jones'
            password = 'password'
            user = Caregiver(email=email, password=password, first_name=first_name, last_name=last_name)
            user.save()
	    caregiver = Caregiver.objects.get(email=email)

	    self.assertEqual(str(caregiver.first_name), first_name)
            self.assertEqual(str(caregiver.last_name), last_name)
            self.assertEqual(str(caregiver.email), email)
            self.assertEqual(Caregiver.objects.count(), 1)









