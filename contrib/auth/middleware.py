import re

from django.conf import settings
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required

class RequireLoginMiddleware(object):
    """
    Middleware component that wraps the login_required decorator around 
    matching URL patterns. To use, add the class to MIDDLEWARE_CLASSES and 
    define LOGIN_REQUIRED_URLS and LOGIN_REQUIRED_URLS_EXCEPTIONS in your 
    settings.py. For example:
    ------
    LOGIN_REQUIRED_URLS = (
        r'/topsecret/(.*)$',
    )
    LOGIN_REQUIRED_URLS_EXCEPTIONS = (
        r'/topsecret/login(.*)$',
        r'/topsecret/logout(.*)$',
    )
    ------
    LOGIN_REQUIRED_URLS is where you define URL patterns; each pattern must 
    be a valid regex.

    LOGIN_REQUIRED_URLS_EXCEPTIONS is, conversely, where you explicitly 
    define any exceptions (like login and logout URLs).
    """
    def __init__(self):
        self.required = tuple([re.compile(url) for url in settings.LOGIN_REQUIRED_URLS])
        self.exceptions = tuple([re.compile(url) for url in settings.LOGIN_REQUIRED_URLS_EXCEPTIONS])

    def process_view(self, request, view_func, view_args, view_kwargs):
        if request.user.is_authenticated(): return None

        for url in self.exceptions:
            if url.match(request.path): return None

        for url in self.required:
            if url.match(request.path): return login_required(view_func)(request, *view_args, **view_kwargs)

        return None

