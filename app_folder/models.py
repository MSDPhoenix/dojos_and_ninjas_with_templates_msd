from django.db import models
from django.db.models.fields import CharField

class Dojo(models.Model):
    name = CharField(max_length=255)
    city = CharField(max_length=255)
    state = CharField(max_length=2)

class Ninja(models.Model):
    first_name = CharField(max_length=255)
    last_name = CharField(max_length=255)
    dojo = models.ForeignKey(Dojo,related_name="ninjas",on_delete = models.CASCADE)
    