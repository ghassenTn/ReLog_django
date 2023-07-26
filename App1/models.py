# models.py

from django.db import models

class Client(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    useragent = models.CharField(max_length=200,default='None')
    ip = models.GenericIPAddressField(default='None')


    def __str__(self):
        return self.name
