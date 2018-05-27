"""django_cms URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path, include
from cms.views import admin

urlpatterns = [
    path('admin', include([
        path('/login', admin.login, name='admin_login'),
        path('/admins', admin.index_or_create, name='admin_index_or_create'),
        path('/admins/<int:admin_id>', admin.detail, name='admin_detail'),
        path('/admins/<int:admin_id>/update', admin.update, name='admin_update'),
        path('/admin_create', admin.get_create, name='admin_get_create'),
        path('/logout',admin.logout,name='admin_logout')
    ]))
]
