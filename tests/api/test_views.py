from django.urls import reverse
from rest_framework.test import APIClient, APITestCase

from api.models import Task


class TestApiViews(APITestCase):

    def setUp(self) -> None:
        self.client = APIClient()

        Task.objects.create(name="Wash utensils")

    def test_task_list(self):
        """Test retrieval of all tasks"""
        response = self.client.get(reverse("task-list-create"))

        self.assertEqual(response.status_code, 200)

    def test_task_creation(self):
        """Test task creation"""
        response = self.client.post(reverse("task-list-create"), data={"name": "Listen to music"})

        self.assertEqual(response.status_code, 201)

    def test_task_retrieval_by_id(self):
        """Test task retrieval by id"""
        response = self.client.get(reverse("task-detail", kwargs={"pk": 1}))

        self.assertEqual(response.status_code, 200)

    def test_task_update(self):
        """Test update task"""
        response = self.client.put(reverse("task-detail", kwargs={"pk": 1}), data={"name": "Go to shop"})

        task = Task.objects.get(id=1)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(task.name, "Go to shop")

    def test_task_deletion(self):
        """Test task delete"""
        response = self.client.delete(reverse("task-detail", kwargs={"pk": 1}))

        self.assertEqual(response.status_code, 204)
