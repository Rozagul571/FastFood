# from django.test import TestCase, Client
# from rest_framework import status
# from .models import User
# from .serializers import UserSerializer
#
# class UserTests(TestCase):
#     def setUp(self):
#         self.client = Client()
#         self.user_data = {
#             'role': 'User',
#             'email': 'test@example.com',
#             'phone_number': '+998901234567',
#             'password_hash': 'testpass',
#             'language': 'uz'
#         }
#
#     def test_user_creation(self):
#         response = self.client.post('/api/users/', self.user_data, format='json')
#         self.assertEqual(response.status_code, status.HTTP_201_CREATED)
#         self.assertEqual(User.objects.count(), 1)
#
#     def test_token_obtain(self):
#         User.objects.create(**self.user_data)
#         response = self.client.post('/api/token/', {'username': 'testuser', 'password': 'testpass'}, format='json')
#         self.assertEqual(response.status_code, status.HTTP_200_OK)
#         self.assertIn('access', response.data)