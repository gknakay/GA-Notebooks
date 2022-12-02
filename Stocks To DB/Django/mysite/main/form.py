# -*- coding: utf-8 -*-

from django import forms

class CreateNewList(forms.Form):
    name = forms.CharField(label = "name", max_length = 50)
    check = forms.BooleanField(required = False)