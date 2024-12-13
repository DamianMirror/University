from rest_framework.test import APITestCase
from rest_framework import status
from university.repositories import Repository


class APITestCase(APITestCase):
    def setUp(self):
        self.user = Repository.Users.create(
            email="apitest@example.com",
            name="API",
            surname="User",
            age=25,
            password="password123"
        )
        self.subject = Repository.Subjects.create(name="Physics")

    def test_get_all_subjects(self):
        response = self.client.get('/subjects/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['name'], "Physics")

    def test_create_subject(self):
        response = self.client.post('/subjects/create/', {"name": "Mathematics"})
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['name'], "Mathematics")

    def test_get_subject_by_id(self):
        response = self.client.get(f'/subjects/{self.subject.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], "Physics")

    def test_create_user(self):
        response = self.client.post('/users/create/', {
            "name": "Test",
            "surname": "User",
            "email": "newuser@example.com",
            "password": "securepassword",
            "age": 30
        })
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['email'], "newuser@example.com")
