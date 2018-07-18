# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse

def index(request):
    response = "Index Route is Working!"
    return HttpResponse(response)