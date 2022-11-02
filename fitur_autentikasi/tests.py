from django.test import TestCase, Client
from django.contrib.auth import authenticate, get_user_model

from fitur_autentikasi.models import Profile
from fitur_autentikasi.forms import *

c = Client()
# Create your tests here.
class FiturAutentikasiTest(TestCase):
    def test_url_register_exist(self):
        response = c.get("/register/")
        self.assertEqual(response.status_code, 200)

    def test_url_login_exist(self):
        response = c.get("/login/")
        self.assertEqual(response.status_code, 200)

    def test_url_logout_exist(self):
        response = c.get("/logout/")
        self.assertEqual(response.status_code, 302)
    
    def test_register_template(self):
        response = c.get("/register/")
        self.assertTemplateUsed(response, "register.html")

    def test_login_template(self):
        response = c.get("/login/")
        self.assertTemplateUsed(response, "login.html")

class SigninTest(TestCase):
    """
    source: https://mkdev.me/posts/how-to-cover-django-application-with-unit-tests
    """

    def setUp(self):
        self.user = get_user_model().objects.create_user(username='test', password='12test12', email='test@example.com')
        self.user.save()

    def tearDown(self):
        self.user.delete()

    def test_correct(self):
        user = authenticate(username='test', password='12test12')
        self.assertTrue((user is not None) and user.is_authenticated)

    def test_wrong_username(self):
        user = authenticate(username='wrong', password='12test12')
        self.assertFalse(user is not None and user.is_authenticated)

    def test_wrong_pssword(self):
        user = authenticate(username='test', password='wrong')
        self.assertFalse(user is not None and user.is_authenticated)

class ProfileTestCase(TestCase):

    def setUp(self):
        self.user = get_user_model().objects.create_user(username='test', password='12test12', email='test@example.com')
        Profile.objects.filter(user=self.user).update(user=self.user, telephone="08123456789", whatsapp="08123456789", line="testline", poin=0)

        self.user.save()
        self.user.profile.save()

    def tearDown(self):
        self.user.delete()

    def test_profile_created(self):
        self.assertTrue(self.user.profile)

    def test_set_poin(self):
        poin = 100
        self.user.profile.set_poin(poin)
        
        self.assertEqual(self.user.profile.poin, poin)

    def test_add_poin(self):
        poin = 100
        self.user.profile.set_poin(0)
        self.user.profile.add_poin(poin)

        self.assertEqual(self.user.profile.poin, poin)
    
    def test_fullname(self):
        fullname = self.user.profile.get_fullname()
        self.assertEqual(f"{self.user.first_name} {self.user.last_name}", fullname)
    
    def test_email(self):
        email = self.user.profile.get_email()
        self.assertEqual(self.user.email, email)

class ProfileFormTestCase(TestCase):

    def setUp(self):
        self.user = get_user_model().objects.create_user(username='test', password='12test12', email='test@example.com')
        self.user.save()

        self.profile_form = ProfileForm(data={'telephone':"08123456789", 'whatsapp':"08123456789", 'line':"testline"}, instance=self.user)
        self.profile_form.save()

    def tearDown(self):
        self.user.delete()
    
    def test_profile_form(self):
        self.assertTrue(self.profile_form)
    
    def test_wrong_telephone(self):
        profile_form = ProfileForm(data={'telephone':"0", 'whatsapp':"08123456789", 'line':"testline"}, instance=self.user)

        self.assertEqual(profile_form.errors['telephone'], ["Nomor telepon tidak valid!"])

    def test_wrong_whatsapp(self):
        profile_form = ProfileForm(data={'telephone':"08123456789", 'whatsapp':"0", 'line':"testline"}, instance=self.user)

        self.assertEqual(profile_form.errors['whatsapp'], ["Nomor Whatsapp tidak valid!"])
    
class UserFormTestCase(TestCase):
    def setUp(self):
        self.user_form = UserForm({'username':'test', 'password1':'12test12', 'password2':'12test12', 'first_name':'first', 'last_name':'last', 'email':'test@example.com'})
        self.user = self.user_form.save()

    def tearDown(self):
        self.user.delete()
    
    def test_email_exist(self):
        user_form = UserForm({'username':'test', 'password1':'12test12', 'password2':'12test12', 'first_name':'first', 'last_name':'last', 'email':'test@example.com'})

        self.assertEqual(user_form.errors["email"], ['Email sudah terdaftar'])