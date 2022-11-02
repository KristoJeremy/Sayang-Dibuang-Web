from django.test import TestCase, Client
from multiprocessing.connection import Client
from django.urls import resolve, reverse
from leaderboard.models import *
from fitur_autentikasi.models import Profile, User
from leaderboard.forms import *
from leaderboard.urls import *

class LeaderboardTest(TestCase):

    # test url
    
    def test_leaderboard(self):
        self.client.user = User.objects.create_user('test', 'test@test.com', 'testpasword')
        self.client.login(username='test', password='testpasword')
        response_x = self.client.get(('/leaderboard/'))
        self.assertEqual(response_x.status_code, 200)

    def test_json(self):
        response_x = self.client.get(reverse('leaderboard:show_json'))
        self.assertEqual(response_x.status_code, 200)

    def test_json_message(self):
        self.client.user = Message(random_message='test')
        self.client.user.save()
        response_x = self.client.get(reverse('leaderboard:show_message_json'))
        self.assertEqual(response_x.status_code, 200)

    def test_add_message(self):
        self.client.user = Message(random_message='test')
        self.client.user.save()
        response_x = self.client.get(reverse('leaderboard:add_message'))
        self.assertEqual(response_x.status_code, 201)
    
 