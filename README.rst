===================
django-get-autologin
===================

django-get-autologin is a simple Django app to login with GET request type that it use Token parameter. 

Installation
------------
Install package from PYPI:
::
    pip install django-get-autologin

or clone and install from repository:
::    
    git clone git@github.com:mazlumagar/django-get-autologin.git
    cd django-get-autologin
    python setup.py install    

Configurations
--------------

Add "get_autologin" to your INSTALLED_APPS setting like this:
::    
    INSTALLED_APPS = [
        ...
        'get_autologin',
    ]
    
Include the polls URLconf in your project urls.py like this:
::    
    from django.conf.urls import url, include
    url(r'^get-autologin/', include('get_autologin.urls', namespace='get_autologin')),

P.S: This namespace important for test.

Settings.py
-----------

Override AUTHENTICATION_BACKENDS
::
    AUTHENTICATION_BACKENDS = [
        'get_autologin.backends.UrlTokenBackend',
        'django.contrib.auth.backends.ModelBackend'
    ]

Define LOGIN_URL and LOGIN_REDIRECT_URL (You have to define)
::
    LOGIN_URL = "your-login-url"
    LOGIN_REDIRECT_URL = "your-login-redirect-url"

Migrate
-------

Run `python manage.py migrate` to create the get_autologin models.

That's all. 


Admin Page
----------

Tokens are managed in admin page. Sample management page:

    http://example.com/admin/get_autologin/token/


Example Request
---------------
    http://example.com/get-autologin/?token={token}

If the token parameter is correct when this request is made, it means that you have logged in as a user who has this token.
