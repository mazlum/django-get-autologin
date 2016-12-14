from django.contrib.auth import authenticate, login
from django.conf import settings
from django.shortcuts import redirect


def user_auth(request):
    if request.user.is_authenticated():
            return redirect(settings.LOGIN_REDIRECT_URL)

    token = request.GET.get('token')
    if not token:
        return redirect(settings.LOGIN_URL)

    user = authenticate(token=token)
    if user is not None:
        login(request, user)
        return redirect(settings.LOGIN_REDIRECT_URL)

    return redirect(settings.LOGIN_URL)
