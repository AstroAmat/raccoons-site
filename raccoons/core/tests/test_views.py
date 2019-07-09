"""View testing for core app"""

from django.test import Client, TestCase
from django.urls import reverse_lazy


class ViewTestCase(TestCase):
    """Class that contains core app tests for views"""

    def setUp(self):
        """Initial configuration for view test case"""
        self.client = Client()

    def test_index_view(self):
        """Tests that index core view is working"""
        path = reverse_lazy('core:index')
        res = self.client.get(path)

        self.assertEqual(res.status_code, 200)
