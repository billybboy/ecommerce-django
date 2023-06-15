"""
Tests for models
"""

from django.test import TestCase
from django.contrib.auth import get_user_model



def create_user(email='user@example.com', password='test444'):

    return get_user_model().objects.create_user(email, password)


class ModelTests(TestCase):

    def test_create_user_with_email_successful(self):
        email = 'user@example.com'
        password = 'test444'
        user = get_user_model().objects.create_user(
            email=email,
            password=password
            )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_user_email_normalized(self):
        """Test normalized email for user"""
        sample_email = [
            ['test1@EXAMPLE.com', 'test1@example.com'],
            ['test2@Example.com', 'test2@example.com'],
            ['TEST3@EXAMPLE.com', 'TEST3@example.com'],
            ["test4@example.COM", 'test4@example.com']
        ]
        for email, expected in sample_email:
            user = get_user_model().objects.create_user(email, 'sample123')
            self.assertEqual(user.email, expected)
