from django.db import models


class Subscribers(models.Model):
    email = models.CharField(max_length=255)
    subscribed_date = models.DateTimeField('Date subscribed')


class MailingLists(models.Model):
    name = models.CharField(max_length=50)
    subscriber = models.ForeignKey(Subscribers)
