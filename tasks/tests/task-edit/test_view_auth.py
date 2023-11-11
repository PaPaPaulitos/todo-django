from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse

from faker import Faker

from tasks.models import Task

fake = Faker()

class TaskTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user('john', 'john@example.com', 'johnpassword')
        self.task = Task.objects.create(title="Test Task", description="Test Description", user=self.user)
    
    def test_status_code_200_after_authentication(self):
        self.client.login(username='john', password='johnpassword')
        response = self.client.get(reverse('edit-task', args=[self.task.id]))
        self.assertEquals(response.status_code, 200)

    def test_template_used_after_authentication(self):
        self.client.login(username='john', password='johnpassword')
        response = self.client.get(reverse('edit-task', args=[self.task.id]))
        self.assertTemplateUsed(response, 'tasks/edittask.html')

    