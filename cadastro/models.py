from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Atleta(models.Model):
    """Atleta"""
    name = models.CharField(max_length=200)

class Graduacao(models.Model):
    """Atleta Graduacao"""
    name = models.CharField(max_length=200)
