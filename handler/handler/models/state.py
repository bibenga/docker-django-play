import ast

from django.contrib.gis.db import models
from django.core.exceptions import ValidationError


class ImportState(models.Model):
    sensor = models.CharField(max_length=50, unique=True)
    moment = models.DateTimeField(null=True, blank=True)
