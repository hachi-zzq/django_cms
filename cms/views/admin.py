from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from cms.models import *
from django.core.paginator import Paginator
from cms import form
from cms.auth import *


def index_or_create(request: HttpRequest):
    """
    index or create
    :param request:
    :return:
    """
    if request.method == 'GET':
        return index(request)

    if request.method == 'POST':
        return create(request)


def index(request: HttpRequest):
    """
    admin index
    :param request:
    :return:
    """

    admins = Admin.objects.all()
    page = request.GET.get('page', default=1)
    per_page = request.GET.get('per_page', default=10)

    paginator = Paginator(admins, per_page=per_page)

    admins = paginator.get_page(page)

    return render(request, template_name='admin/admin_index.html', context={
        'admins': admins
    })


def get_create(request: HttpRequest):
    return render(request, template_name='admin/admin_create.html')


def detail(request: HttpRequest, admin_id):
    """
    admin detail
    :param request:
    :param admin_id:
    :return:
    """
    try:
        admin = Admin.objects.get(id=admin_id)
    except Exception as e:
        return HttpResponse(str(e))

    return render(request, 'admin/admin_detail.html', context={
        "admin": admin
    })


def create(request: HttpRequest):
    """
    admin index
    :param request:
    :return:
    """
    f = form.AdminCreate(request.POST)
    if not f.is_valid():
        return HttpResponse(f.errors.items())

    name = f.cleaned_data['name']
    password = f.cleaned_data['password']

    Admin.objects.create(name=name, password=password)
    return redirect('/admin/admins')


def update(request: HttpRequest, admin_id):
    """
    update admin
    :param request:
    :param admin_id:
    :return:
    """
    f = form.AdminUpdate(request.POST)
    if not f.is_valid():
        return HttpResponse(f.errors.items())

    try:
        admin = Admin.objects.get(id=admin_id)
    except Exception as e:
        return HttpResponse(str(e))

    if f.cleaned_data['name']:
        admin.name = f.cleaned_data['name']

    if f.cleaned_data['password']:
        admin.password = f.cleaned_data['password']

    admin.save()

    return redirect('/admin/admins')


def delete(request: HttpRequest, admin_id):
    """
    delete admin
    :param request:
    :param admin_id:
    :return:
    """
    return HttpResponse(admin_id)


def disable(request: HttpRequest, admin_id):
    """
    disable admin
    :param request:
    :param admin_id:
    :return:
    """
    pass


def login(request: HttpRequest):
    """
    login admin
    :param request:
    :return:
    """
    if request.method == 'GET':
        return get_login(request)
    return post_login(request)


def get_login(request: HttpRequest):
    return render(request, 'admin/login.html')


def post_login(request: HttpRequest):
    name = request.POST.get('name')
    password = request.POST.get('password')
    import logging
    logger = logging.getLogger('django')
    logger.info((name,password))
    admin = Admin.objects.filter(name=name).filter(password=password).order_by('id').first()
    if admin:
        login_admin(request,admin.id)
        return redirect('/admin/admins')
    else:
        raise PermissionError()


def logout(request: HttpRequest):
    """
    logout admin
    :param request:
    :return:
    """
    pass
