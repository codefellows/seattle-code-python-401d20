from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Snack

"""
WARNING ONE:
Use local SQLite Database when testing.
Easiest way to do this is to comment out the
DATABASE_* lines in .env

It's possible to test with remote database,
but not on the free plan we're using in class.

WARNING TWO:
Make sure your url names are unique.
For example, your api list url cannot have same name as front end url.
Easiest way to handle is to name api urls with api in the name
E.g.  "snack_api_list" for api, and "snack_list" for front end

"""


class SnackTests(APITestCase):
    @classmethod
    def setUpTestData(cls):
        testuser1 = get_user_model().objects.create_user(
            username="testuser1", password="pass"
        )
        testuser1.save()

        test_snacks = Snack.objects.create(
            name="avocado",
            snacker=testuser1,
            fave=True,
        )
        test_snacks.save()

    # class 32
    def setUp(self):
        self.client.login(username="testuser1", password="pass")

    def test_snacks_model(self):
        snack = Snack.objects.get(id=1)
        actual_snacker = str(snack.snacker)
        actual_name = str(snack.name)
        actual_fave = bool(snack.fave)
        self.assertEqual(actual_snacker, "testuser1")
        self.assertEqual(actual_name, "avocado")
        self.assertEqual(
            actual_fave, True
        )

    def test_get_snack_list(self):
        url = reverse("snack_api_list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        snacks = response.data
        self.assertEqual(len(snacks), 1)
        self.assertEqual(snacks[0]["name"], "avocado")

    def test_get_snack_by_id(self):
        url = reverse("snack_api_detail", args=(1,))
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        snack = response.data
        self.assertEqual(snack["name"], "avocado")

    def test_create_snack(self):
        url = reverse("snack_api_list")
        data = {"snacker": 1, "name": "coconut", "fave": False}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        snacks = Snack.objects.all()
        self.assertEqual(len(snacks), 2)
        self.assertEqual(Snack.objects.get(id=2).name, "coconut")

    def test_update_snack(self):
        url = reverse("snack_api_detail", args=(1,))
        data = {
            "snacker": 1,
            "name": "avocado",
            "fave": False,
        }
        response = self.client.put(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        snack = Snack.objects.get(id=1)
        self.assertEqual(snack.name, data["name"])
        self.assertEqual(snack.snacker.id, data["snacker"])
        self.assertEqual(snack.fave, data["fave"])

    def test_delete_snack(self):
        url = reverse("snack_api_detail", args=(1,))
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        snacks = Snack.objects.all()
        self.assertEqual(len(snacks), 0)

    # class 32
    def test_authentication_required(self):
        self.client.logout()
        url = reverse("snack_api_list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
