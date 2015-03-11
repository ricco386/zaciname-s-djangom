# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse(u'Ahoj Svet. Práve sa nachádzame v mailinglistovom indexe.')

def mlist(request, list_id):
    return HttpResponse(u'Práve sa nachádzame v mailinglite %s.' % list_id)

def subscribe(request, list_id):
    return HttpResponse(u'Práve sa zapisujete do mailinglistu %s.' % list_id)
