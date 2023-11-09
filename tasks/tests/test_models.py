from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from faker import Faker

from ..models import Task

User = get_user_model()
fake = Faker()

class TaskTestCase(TestCase):
    def setUp(self):
        
        self.user = User.objects.create_user(username=fake.user_name())

        self.title = fake.name()
        self.description = fake.text()
        self.done = "doing",
        

        self.object = Task.objects.create(
            title=self.title,
            description=self.description,
            done=self.done,
            user=self.user,
        )

    def test_title_is_equal_str_return(self):
        self.assertEquals(self.object.__str__(), self.title)

    def test_description_is_equal(self):
        self.assertEquals(self.object.description, self.description)

    def test_done_is_equal(self):
        self.assertEquals(self.object.done, self.done)

    def test_user_is_equal(self):
        self.assertEquals(self.object.user, self.user)


