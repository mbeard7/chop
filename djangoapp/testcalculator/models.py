from __future__ import unicode_literals

from django.db import models

# Create your models here.
class user(models.Model):
    user_No = models.AutoField(primary_key=True)
    user_ID = models.CharField(null=False,unique=True,max_length=24)
    name = models.CharField(max_length=240)
    # TODO: Validate the email field
    email = models.CharField(null=False,unique=True,max_length=240)
    # TODO: Convert institution to a foreign key
    institution = models.CharField(max_length=240)
    # TODO: ALlow null here
    trainee_stage = models.CharField(max_length=240)

class institution(models.Model):
    name = models.CharField(null=False,unique=True,max_length=240)

class test(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(null=False,unique=True,max_length=240)
    # TODO: ALlow null here
    abbrev = models.CharField(max_length=10)
    # TODO: ALlow null here
    synonym = models.CharField(max_length=240)
    cost = models.IntegerField(null=False)
