from http import HTTPStatus
from django.test import TestCase, Client

from crowdfunding.models import Crowdfund
from .forms import CrowdfundForm
from fitur_autentikasi.models import Profile
from django.contrib.auth import get_user_model

# Create your tests here.
class CrowdfundTestCase(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username="test", password="weyyyyy", email="test@test.com"
        )
        Profile.objects.filter(user=self.user).update(telephone="08123123123")
        self.client = Client()
        self.client.login(username="test", password="weyyyyy")
        self.user.save()
        self.user.profile.save()

        self.user2 = get_user_model().objects.create_user(
            username="test2", password="weyyyyy", email="test@test.com"
        )
        Profile.objects.filter(user=self.user2).update(telephone="08123123123")
        self.client2 = Client()
        self.client2.login(username="test2", password="weyyyyy")
        self.user2.save()
        self.user2.profile.save()

    # forms.py tests
    def test_form_is_valid(self):
        form = CrowdfundForm(
            data={
                "user": self.user,
                "title": "Title",
                "description": "Description",
                "received": 0,
                "target": 100,
            }
        )
        self.assertTrue(form.is_valid())

    def test_target_is_less_than_received(self):
        form = CrowdfundForm(
            data={
                "user": self.user,
                "title": "Title",
                "description": "Description",
                "received": 10,
                "target": 1,
            }
        )
        self.assertFalse(form.is_valid())

    def test_received_is_negative(self):
        form = CrowdfundForm(
            data={
                "user": self.user,
                "title": "Title",
                "description": "Description",
                "received": -1,
                "target": 2,
            }
        )
        self.assertFalse(form.is_valid())

    def test_target_is_zero(self):
        form = CrowdfundForm(
            data={
                "user": self.user,
                "title": "Title",
                "description": "Description",
                "received": 0,
                "target": 0,
            }
        )
        self.assertFalse(form.is_valid())

    # views.py tests
    def test_show_crowdfundings(self):
        res = self.client.get("/crowdfundings/")
        self.assertEqual(res.status_code, HTTPStatus.OK)

    def test_create_crowdfund(self):
        res = self.client.post(
            "/crowdfundings/create/",
            {
                "title": "Title",
                "description": "Description",
                "received": 0,
                "target": 100,
            },
            follow=True,
        )
        self.assertEqual(res.status_code, HTTPStatus.OK)

    def test_open_create_crowdfund_page(self):
        res = self.client.get("/crowdfundings/create/")
        self.assertEqual(res.status_code, HTTPStatus.OK)

    def test_open_crowdfund_by_id_page(self):
        Crowdfund.objects.create(
            id=1, title="test", description="test", received="1", target="12"
        )
        res = self.client.get("/crowdfundings/1/")
        self.assertEqual(res.status_code, HTTPStatus.OK)

    def test_open_edit_crowdfund_page(self):
        Crowdfund.objects.create(
            user=self.user.profile,
            id=1,
            title="test",
            description="test",
            received=1,
            target=12,
        )
        res = self.client.get("/crowdfundings/edit/1")
        self.assertEqual(res.status_code, HTTPStatus.OK)

    def test_edit_crowdfund_(self):
        Crowdfund.objects.create(
            user=self.user.profile,
            id=1,
            title="test",
            description="test",
            received=1,
            target=12,
        )
        res = self.client.post("/crowdfundings/edit/1", {"received": 1, "target": 100})
        self.assertEqual(res.status_code, HTTPStatus.OK)

    def test_delete_crowdfund(self):
        Crowdfund.objects.create(
            user=self.user.profile,
            id=1,
            title="test",
            description="test",
            received=1,
            target=12,
        )
        res = self.client.post("/crowdfundings/delete/1")
        self.assertEqual(res.status_code, HTTPStatus.OK)

    def test_show_crowdfundings_json(self):
        Crowdfund.objects.create(
            user=self.user.profile,
            id=1,
            title="test",
            description="test",
            received=1,
            target=12,
        )
        Crowdfund.objects.create(
            user=self.user.profile,
            id=2,
            title="test",
            description="test",
            received=1,
            target=12,
        )
        res = self.client.get("/crowdfundings/json/")
        self.assertEqual(res.status_code, HTTPStatus.OK)

    def test_show_crowdfunding_by_id_json(self):
        Crowdfund.objects.create(
            user=self.user.profile,
            id=1,
            title="test",
            description="test",
            received=1,
            target=12,
        )
        res = self.client.get("/crowdfundings/json/1")
        self.assertEqual(res.status_code, HTTPStatus.OK)

    def test_add_point_when_contacting(self):
        Crowdfund.objects.create(
            user=self.user2.profile,
            id=1,
            title="test",
            description="test",
            received=1,
            target=12,
        )

        res = self.client.get("/crowdfundings/add-point-when-contacting/1")
        self.assertEqual(res.status_code, HTTPStatus.OK)
