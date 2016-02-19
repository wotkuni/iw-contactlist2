from __future__ import unicode_literals

from django.db import models


class Contact(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)