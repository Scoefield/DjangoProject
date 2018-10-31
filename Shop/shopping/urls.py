# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     urls
   Author :       hyt
   Create date：          2018/10/31
-------------------------------------------------
"""
from django.urls import path
from . import views

app_name = 'shopping'
urlpatterns = [
    path('', views.home, name='home'),
    path('<phone_id>/', views.single_web, name='single_web'),
    path('<phone_id>/<good_id>/', views.good_detail, name='good_detail')
]
