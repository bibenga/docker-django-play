from django.contrib import admin

from handler.models import Sensor2Rule


@admin.register(Sensor2Rule)
class Sensor2RuleAdmin(admin.ModelAdmin):
    model = Sensor2Rule
    list_display = ('id', 'code', 'value_expr')
    list_filter = ('code',)
