from django.http import HttpRequest, HttpResponse
from django.core.exceptions import PermissionDenied, MiddlewareNotUsed
from .auth import *
from django.shortcuts import redirect


class AdminAuth:
    EXCEPT = [
        r'/admin/login'
    ]

    def __init__(self, get_response):
        self.get_response = get_response
        # One-time configuration and initialization.

    def __call__(self, request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.

        response = self.get_response(request)

        # Code to be executed for each request/response after
        # the view is called.

        return response

    @classmethod
    def process_view(cls, request: HttpRequest, view_func, view_args, view_kwargs):
        if request.path in cls.EXCEPT:
            return None
        if not admin_is_login(request):
            return redirect('/admin/login')
        return None

    @classmethod
    def process_template_response(cls, request:HttpRequest, response:HttpResponse):
        import logging
        logger = logging.getLogger('django')
        logger.info(response)
        pass
