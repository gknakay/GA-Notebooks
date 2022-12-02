# -*- coding: utf-8 -*-
"""
Created on Wed Feb 23 13:09:57 2022

@author: Gökhan Akay
"""

from django.urls import path
from main import views

urlpatterns = [
path("<int:id>", views.index, name = 'index'),
path("", views.home, name = 'home'),
path("create/", views.create, name = 'create'),
]