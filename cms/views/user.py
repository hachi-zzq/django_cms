from django.shortcuts import HttpResponse
from django.http import HttpRequest

"""
user view
"""


def user(request: HttpRequest):
    method = request.method
    function = 'user_' + str.lower(method)

    return eval(function)(request)


def user_get(request: HttpRequest):
    return HttpResponse('index')


def user_post(reqest: HttpRequest):
    return HttpResponse('create')


