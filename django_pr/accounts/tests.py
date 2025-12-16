from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User

class AuthViewsTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password='testpass123')

    def test_home_access(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)

    def test_protected_redirects_unauthenticated(self):
        response = self.client.get(reverse('protected'))
        self.assertEqual(response.status_code, 302)
        self.assertIn('/login/', response.url)

    def test_login_works(self):
        response = self.client.post(reverse('login'), {
            'username': 'testuser',
            'password': 'testpass123'
        })
        self.assertRedirects(response, reverse('home'))

    def test_register_and_login(self):
        response = self.client.post(reverse('register'), {
            'username': 'newuser',
            'password1': 'strongpass123!',
            'password2': 'strongpass123!'
        })
        self.assertRedirects(response, reverse('home'))
        self.assertTrue(User.objects.filter(username='newuser').exists())

