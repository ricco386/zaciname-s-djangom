# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse(u'Ahoj Svet. Práve sa nachádzame v mailinglistovom indexe.')
