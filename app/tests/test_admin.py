"""
Tests for the Django admin
"""

from django.contrib.auth import get_user_model
from django.test import TestCase, Client
from django.urls import reverse


class AdminSiteTest(TestCase):

    def setUp(self):
        """Set superuser and user"""
        self.client = Client()
        self.admin_user = get_user_model().objects.create_superuser(
            email='admin@example.com',
            password='test1234'
        )
        self.client.force_login(self.admin_user)
        self.user = get_user_model().objects.create_user(
            email='user@example.com',
            password='test1234',
            name='Test User'
        )

    def test_get_user_list(self):
        """ Show user list"""
        url = reverse('admin:app_user_changelist')
        res = self.client.get(url)

        self.assertContains(res, self.user.name)
        self.assertContains(res, self.user.email)

    def test_add_user(self):
        """Test the create user page"""
        url = reverse('admin:app_user_add')
        res = self.client.get(url)

        self.assertEqual(res.status_code, 200)

    def test_edit_user(self):
        """Test the edit user page"""
        url = reverse('admin:app_user_change', args=[self.user.id])
        res = self.client.get(url)

        self.assertEqual(res.status_code, 200)
