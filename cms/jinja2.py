from django.contrib.staticfiles.storage import staticfiles_storage
from django.urls import reverse
from jinja2 import Environment
from datetime import datetime


def environment(**options):
    env = Environment(**options)
    env.globals.update({
        'static': staticfiles_storage.url,
        'url': reverse,
    })
    env.filters['date_format'] = date_format
    return env


def date_format(date_value: datetime):
    """
    时间格式化
    :param date_value:
    :return:
    """
    return date_value.strftime('%Y-%m-%d %H:%M:%S')
