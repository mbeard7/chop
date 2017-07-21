from __future__ import unicode_literals

from django.db import models

# Create your models here.

class test(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(null=False,unique=True,max_length=240)
    # TODO: ALlow null here
    abbrev = models.CharField(max_length=10)
    # TODO: ALlow null here
    synonym = models.CharField(max_length=240)
    cost = models.IntegerField(null=False)
