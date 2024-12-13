
from django.test import TestCase
from university.models import User, Student, Teacher, Subject, Mark
from university.repositories import Repository


class RepositoriesTestCase(TestCase):
    def setUp(self):
        self.user = Repository.Users.create(
            email="test@example.com", name="Test", surname="User", age=25, password="password123"
        )
        self.subject = Repository.Subjects.create(name="Mathematics")
        self.group = Repository.StudentGroups.create(name="Group A")
        self.teacher_user = Repository.Users.create(email="teacher@example.com", name="Teacher", surname="User", age=30, password="password123")
        self.teacher = Repository.Teachers.create(user=self.teacher_user, salary=1000)

    def test_get_user_by_id(self):
        user = Repository.Users.get_by_id(self.user.id)
        self.assertEqual(user.email, "test@example.com")

    def test_delete_user(self):
        Repository.Users.delete(self.user.id)
        user = Repository.Users.get_by_id(self.user.id)
        self.assertIsNone(user)

    def test_update_user(self):
        updated_user = Repository.Users.update(self.user.id, name="Updated")
        self.assertEqual(updated_user.name, "Updated")

    def test_create_teacher(self):
        teacher = Repository.Teachers.create(user=self.user, salary=1000)
        self.assertEqual(teacher.salary, 1000)

    def test_get_teacher_by_id(self):
        teacher = Repository.Teachers.create(user=self.user, salary=1000)
        fetched_teacher = Repository.Teachers.get_by_id(teacher.user)
        self.assertEqual(fetched_teacher.salary, 1000)

    # def test_mark_creation(self):
    #     student = Repository.Students.create(user=self.user, group_id=None)
    #     mark = Mark.objects.create(student=student, subject=self.subject, value=85, teacher=self.teacher, type=1)
    #     self.assertEqual(mark.value, 85)

    def test_get_subjects(self):
        subjects = Repository.Subjects.get_all()
        self.assertGreaterEqual(len(subjects), 1)
