from django.http import HttpRequest

USER_LOGIN_SESSION_KEY = 'user_id'


def user_is_login(request: HttpRequest):
    """
    前台是否登录
    :param request:
    :return:
    """
    return request.session.get(USER_LOGIN_SESSION_KEY)


def login_user(request: HttpRequest, user_id):
    """
    登录前台用户
    :param request:
    :param user_id:
    :return:
    """
    request.session[USER_LOGIN_SESSION_KEY] = user_id
    return user_id


def logout_user(request: HttpRequest):
    """
    登出前台用户
    :param request:
    :return:
    """
    if user_is_login(request):
        del request.session[USER_LOGIN_SESSION_KEY]

    return True


ADMIN_LOGIN_SESSION_KEY = 'admin_id'


def admin_is_login(request: HttpRequest):
    """
    前台是否登录
    :param request:
    :return:
    """
    return request.session.get(ADMIN_LOGIN_SESSION_KEY)


def login_admin(request: HttpRequest, admin_id):
    """
    登录前台用户
    :param request:
    :param admin_id:
    :return:
    """
    request.session[ADMIN_LOGIN_SESSION_KEY] = admin_id
    return admin_id


def logout_admin(request: HttpRequest):
    """
    登出前台用户
    :param request:
    :return:
    """
    if admin_is_login(request):
        del request.session[ADMIN_LOGIN_SESSION_KEY]

    return True
