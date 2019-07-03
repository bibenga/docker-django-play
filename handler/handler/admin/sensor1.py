from django.contrib import admin

from handler.models import Sensor1Rule


@admin.register(Sensor1Rule)
class Sensor1RuleAdmin(admin.ModelAdmin):
    model = Sensor1Rule
    list_display = ('id', 'code', 'value_expr',)
    list_filter = ('code',)

