from django.contrib.auth.models import AnonymousUser
from django.test import TestCase, RequestFactory, Client
from django.contrib.auth import get_user_model
from django.urls.base import reverse
from django.conf import settings

from .models import Token
from .views import user_auth

UserModel = get_user_model()


class GetAutoAuthTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.factory = RequestFactory()
        self.user = UserModel.objects.create(username="jacob", email="jacob@email.com", password="top_secret")
        self.url_token = Token.objects.create(user=self.user)

    def test_auth(self):
        auth_url = "{0}?token={1}".format(reverse('get_autologin:auth'), self.url_token.token)
        request = self.factory.get(auth_url)
        request.user = AnonymousUser()
        request.session = self.client.session
        response = user_auth(request)
        response.client = self.client
        self.assertRedirects(response, settings.LOGIN_REDIRECT_URL, status_code=302, target_status_code=200)
