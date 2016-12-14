from django.conf.urls import url
from .views import user_auth

urlpatterns = [
    url(r'^$', user_auth, name='auth')
]
