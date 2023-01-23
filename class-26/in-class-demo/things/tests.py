from django.test import SimpleTestCase
from django.urls import reverse


class ThingsTests(SimpleTestCase):
    def test_home_page_status_code(self):
        url = reverse('home')
        print(f'the url is: {url}')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_home_page_template(self):
        url = reverse('home')
        response = self.client.get(url)
        self.assertTemplateUsed(response, 'home.html')
        self.assertTemplateUsed(response, 'base.html')

