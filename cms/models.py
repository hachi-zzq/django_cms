from django.db import models
from django.core.validators import *

class User(models.Model):
    name = models.CharField(max_length=70, db_index=True, unique=True)
    password = models.CharField(max_length=70)

    STATUS_NORMAL = 'NORMAL'
    STATUS_LOCKED = 'LOCKED'
    STATUS = [STATUS_LOCKED, STATUS_NORMAL]

    status = models.CharField(max_length=70, default=STATUS_NORMAL)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'users'


class Article(models.Model):
    title = models.CharField(max_length=70)
    content = models.TextField(max_length=70)
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    class Meta:
        db_table = 'articles'


class Comment(models.Model):
    content = models.TextField(max_length=70)
    status = models.CharField(max_length=70)
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    article = models.ForeignKey(Article, on_delete=models.SET_NULL, null=True)

    class Meta:
        db_table = 'comments'


class Admin(models.Model):
    name = models.CharField(max_length=70,validators=[EmailValidator])
    password = models.CharField(max_length=70)

    STATUS_NORMAL = 'NORMAL'
    STATUS_LOCKED = 'LOCKED'
    STATUS = [STATUS_LOCKED, STATUS_NORMAL]

    status = models.CharField(max_length=70,default=STATUS_NORMAL)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'admins'