#Django 
from django.db import models

class historical(models.Model):
    data = models.CharField(max_length=50, null=False)


class Alphanumeric(models.Model):
    text = models.CharField(max_length=50, null=False)
    initial_letter = models.CharField(max_length=1, null=False)
    final_letter = models.CharField(max_length=1, null=False)
    
    created = models.DateTimeField(auto_now_add = True)
    modified = models.DateTimeField(auto_now = True)


class Number(models.Model):
    number = models.IntegerField(null=False)
    accumulated = models.IntegerField(default=0)


class Special_char(models.Model):
    special_character = models.CharField(max_length=50)
