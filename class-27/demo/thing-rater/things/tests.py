from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse
from .models import Thing


class ThingsTests(TestCase):
    def setUp(self):
        reviewer = get_user_model().objects.create(username="tester",password="tester")
        Thing.objects.create(name="rake", reviewer=reviewer)

    def test_list_page_status_code(self):
        url = reverse('thing_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_list_page_template(self):
        url = reverse('thing_list')
        response = self.client.get(url)
        self.assertTemplateUsed(response, 'thing_list.html')
        self.assertTemplateUsed(response, 'base.html')

    def test_list_page_context(self):
        url = reverse('thing_list')
        response = self.client.get(url)
        things = response.context['object_list']
        self.assertEqual(len(things), 1)
        self.assertEqual(things[0].name, "rake")
        self.assertEqual(things[0].rating, 0)
        self.assertEqual(things[0].reviewer.username, "tester")

    def test_detail_page_status_code(self):
        url = reverse('thing_detail',args=(1,))
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_detail_page_template(self):
        url = reverse('thing_detail',args=(1,))
        response = self.client.get(url)
        self.assertTemplateUsed(response, 'thing_detail.html')
        self.assertTemplateUsed(response, 'base.html')

    def test_detail_page_context(self):
        url = reverse('thing_detail',args=(1,))
        response = self.client.get(url)
        thing = response.context['thing']
        self.assertEqual(thing.name, "rake")
        self.assertEqual(thing.rating, 0)
        self.assertEqual(thing.reviewer.username, "tester")
