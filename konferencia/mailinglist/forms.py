# -*- coding: utf-8 -*-
from django.forms import ModelForm
from mailinglist.models import Subscriber

class SubscribeForm(ModelForm):
    class Meta:
        model = Subscriber
        fields = ('email',)
