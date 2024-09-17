from django.contrib.auth.models import User
from django.urls import reverse

from rest_framework.test import APITestCase
from rest_framework.authtoken.models import Token
from rest_framework import status

from .models import Article


class ArticleAPITestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create(username="test_user")
        self.article = Article.objects.create(
            title="Test Article",
            content="This is a test article.",
            author=self.user,
        )
        self.token = Token.objects.create(user=self.user)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)

    def test_create(self):
        url = reverse('articles')
        response = self.client.post(url, data={'title': 'Test Article', 'content': 'This is a test article.'})
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertGreaterEqual(Article.objects.count(), 1)

    def test_update(self):
        url = reverse('article', kwargs={'pk': self.article.id})
        response = self.client.put(url, data={'title': 'Test Article', 'content': 'This is a test article.'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete(self):
        url = reverse('article', kwargs={'pk': self.article.id})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Article.objects.count(), 0)

    def test_list(self):
        url = reverse('articles')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
