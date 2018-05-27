from django import forms
from django.core.validators import *

class AdminCreate(forms.Form):
    name = forms.EmailField(required=True, error_messages={
        "required": "必须有"
    })
    password = forms.CharField(max_length=70, min_length=6)


class AdminUpdate(forms.Form):
    name = forms.EmailField()
    password = forms.CharField(min_length=None)
