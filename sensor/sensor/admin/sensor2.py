from django.contrib import admin
from django.utils.translation import gettext_lazy

from sensor.models import Sensor2


@admin.register(Sensor2)
class Sensor1Admin(admin.ModelAdmin):
    model = Sensor2
    list_display = ('id', 'code', 'value', 'moment')
    date_hierarchy = 'moment'
    ordering = ('-moment',)
    list_filter = ('moment',)
    search_fields = ('code',)
    fieldsets = (
        (None, {
            'fields': ('code',)
        }),
        (gettext_lazy('Value'), {
            'fields': ('moment', 'value')
        }),
    )
