from django.test import TestCase, TestCase
from django.urls import reverse

from .models import Post

class PostModelTest(TestCase):
    def setUp(self):
        Post.objects.create(text='Just a test')

    def test_post_text(self):
        post = Post.objects.get(id=1)
        self.assertEqual(post.text, 'Just a test')

class HomePageTest(TestCase):
    def test_status_code(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
