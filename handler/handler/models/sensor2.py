import ast

from django.contrib.gis.db import models
from django.core.exceptions import ValidationError


class Sensor2Rule(models.Model):
    code = models.CharField(
        max_length=50,
        unique=True,
        blank=True,
        null=True,
        help_text='Сейчас не учитывается, но например разные версии датчиков имеют разный масштаб'
    )
    value_expr = models.TextField(null=True, blank=True)

    def __str__(self):
        return f'{self.code}'

    def clean(self):
        if self.value_expr:
            try:
                ast.parse(self.value_expr)
            except SyntaxError:
                raise ValidationError({'value_expr': 'syntax error'})

# Используем специальную модельку и для второго сенсора,
# в жизни будут все таки разные модели, но для демо не важно
class Sensor2(models.Model):
    code = models.CharField(max_length=50, db_index=True, help_text='Код датчика или типо того')
    moment = models.DateTimeField(null=False, blank=False, db_index=True)
    value = models.FloatField(default=0.0)

    class Meta:
        managed = False
        db_table = 'sensor_sensor2'

    def __str__(self):
        return f'{self.code}@{self.moment}'
