from django.db import models


class Subscriber(models.Model):
    email = models.CharField(max_length=255)
    subscribed_date = models.DateTimeField('Date subscribed')


class MailingList(models.Model):
    name = models.CharField(max_length=50)
    subscriber = models.ManyToManyField(Subscriber)
