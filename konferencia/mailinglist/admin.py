from django.contrib import admin

from mailinglist.models import Subscriber, MailingList


class SubscriberAdmin(admin.ModelAdmin):
    list_display = ('email', 'subscribed_date')

admin.site.register(Subscriber, SubscriberAdmin)
admin.site.register(MailingList)

