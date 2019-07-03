from django.contrib.gis.db import models


class ResultQuerySet(models.QuerySet):
    pass


class Result(models.Model):
    sensor = models.CharField(max_length=50)
    source_id = models.PositiveIntegerField()

    code = models.CharField(max_length=50, db_index=True, help_text='Код датчика или типо того')
    moment = models.DateTimeField(null=False, blank=False, db_index=True)
    value = models.FloatField(default=0.0)

    objects = ResultQuerySet.as_manager()

    class Meta:
        unique_together = (
            ('sensor', 'source_id'),
        )

    def __str__(self):
        return f'{self.code}@{self.moment}'

