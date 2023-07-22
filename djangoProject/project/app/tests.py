# blog/tests.py

from django.test import TestCase, Client
from django.urls import reverse
from app.models import WriteSomething

class BlogViewTest(TestCase):

    def setUp(self):
        self.client = Client()
        self.blog1 = WriteSomething.objects.create(title='Blog Post 1', content='This is the content of Blog Post 1.')
        self.blog2 = WriteSomething.objects.create(title='Blog Post 2', content='This is the content of Blog Post 2.')

    def test_blog_list_view(self):
        response = self.client.get(reverse('community'))

        self.assertEqual(response.status_code, 200)

        self.assertTemplateUsed(response, 'community.html')