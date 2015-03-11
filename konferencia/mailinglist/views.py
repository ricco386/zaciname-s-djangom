# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse, Http404
from mailinglist.models import MailingList

def index(request):
    return HttpResponse(u'Ahoj Svet. Práve sa nachádzame v mailinglistovom indexe.')

def mlist(request, list_id):
    try:
        ml = MailingList.objects.get(pk=list_id)
    except MailingList.DoesNotExist:
        raise Http404(u'Mailinglist neexistuje!!!')
    return render(request, 'mailinglist/mlist.html', {'ml': ml})

def subscribe(request, list_id):
    return HttpResponse(u'Práve sa zapisujete do mailinglistu %s.' % list_id)
