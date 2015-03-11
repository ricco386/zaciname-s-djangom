# -*- coding: utf-8 -*-
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, Http404
from mailinglist.models import MailingList
from mailinglist.forms import SubscribeForm

def index(request):
    return HttpResponse(u'Ahoj Svet. Práve sa nachádzame v mailinglistovom indexe.')

def mlist(request, list_id):
    try:
        ml = MailingList.objects.get(pk=list_id)
    except MailingList.DoesNotExist:
        raise Http404(u'Mailinglist neexistuje!!!')
    return render(request, 'mailinglist/mlist.html', {'ml': ml})

def subscribe(request, list_id):
    ml = get_object_or_404(MailingList, pk=list_id)

    if request.method == "POST":
        form = SubscribeForm(request.POST)
        if form.is_valid():
            subscriber = form.save()
            ml.subscriber.add(subscriber)
            return redirect('mlist', list_id=list_id)
    else:
        form = SubscribeForm

    return render(request, 'mailinglist/subscribe.html', {'ml': ml, 'form': form})

