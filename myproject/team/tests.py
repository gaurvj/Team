from django.test import TestCase, Client
from django.urls import reverse
from django.urls import resolve
from .models import  Team, Player, PlayerHistory, Match, Point


# Create your tests here.
class TestViews(TestCase):

   def setUp(self):
       self.client = Client()
       self.team = reverse('team')


   def test_home_page(self):
       response = self.client.get(self.team)
       self.assertEqual(response.status_code, 200)
       self.assertTemplateUsed(response, 'home.html')

