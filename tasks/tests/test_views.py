from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse

from faker import Faker

fake = Faker()

class TaskTestCase(TestCase):
    def test_status_code_200_hello_world(self):
        response = self.client.get(reverse('hello-world'))
        self.assertEquals(response.status_code, 200)

    def test_status_code_200_your_name(self):
        text_name = fake.name()
        response = self.client.get(reverse('your-name', args=[text_name]))
        self.assertEquals(response.status_code, 200)

    def test_status_code_302_redirect_if_you_not_authenticated(self):
        response = self.client.get(reverse('tasks-list'))
        self.assertEquals(response.status_code, 302)

    def test_redirect_if_you_not_authenticated(self):
        response = self.client.get(reverse('tasks-list'))
        self.assertRedirects(response, '/accounts/login/?next=/')

    
    def test_redirect_if_you_not_authenticated_template(self):
        response = self.client.get(reverse('tasks-list'), follow=True)
        self.assertTemplateUsed(response, 'registration/login.html')


    