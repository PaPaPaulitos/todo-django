from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse

from faker import Faker

fake = Faker()

class TaskTestCase(TestCase):
    def test_status_code_302_redirect_if_you_not_authenticated(self):
        response = self.client.get(reverse('new-task'))
        self.assertEquals(response.status_code, 302)

    def test_redirect_if_you_not_authenticated(self):
        response = self.client.get(reverse('new-task'))
        self.assertRedirects(response, '/accounts/login/?next=/newtask/')

    
    def test_redirect_if_you_not_authenticated_template(self):
        response = self.client.get(reverse('new-task'), follow=True)
        self.assertTemplateUsed(response, 'registration/login.html')