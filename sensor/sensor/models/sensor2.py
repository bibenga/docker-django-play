from django.contrib.gis.db import models


class Sensor2QuerySet(models.QuerySet):
    pass


class Sensor2(models.Model):
    code = models.CharField(max_length=50, db_index=True, help_text='Код датчика или типо того')
    moment = models.DateTimeField(null=False, blank=False, db_index=True)
    value = models.FloatField(default=0.0)

    objects = Sensor2QuerySet.as_manager()

    def __str__(self):
        return f'{self.code}'
