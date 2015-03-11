from django.contrib import admin
from mailinglist.models import Subscriber, MailingList

admin.site.register(Subscriber)
admin.site.register(MailingList)
