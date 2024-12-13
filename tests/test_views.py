from django.test import TestCase, Client
from django.urls import reverse

from university.repositories import Repository

class ViewsTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = Repository.Users.create(
            email="viewtest@example.com",
            name="View",
            surname="Test",
            age=25,
            password="password123"
        )
        self.group = Repository.StudentGroups.create(name="Group A")
        self.student = Repository.Students.create(user=self.user, group_id=self.group.id)

    def test_home_view(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)

    def test_register_view_get(self):
        response = self.client.get(reverse('register'))
        self.assertEqual(response.status_code, 200)

    def test_register_view_post(self):
        response = self.client.post(reverse('register'), {
            "name": "John",
            "surname": "Doe",
            "email": "johndoe@example.com",
            "password": "securepassword",
            "age": 30
        })
        self.assertEqual(response.status_code, 302)  # Redirect after successful registration

    def test_student_list_view(self):
        response = self.client.get(reverse('get_all_students'))
        print(response.content)
        self.assertEqual(response.status_code, 302)
