from django.contrib import admin

from handler.models.state import ImportState


@admin.register(ImportState)
class ImportStateAdmin(admin.ModelAdmin):
    model = ImportState
    list_display = ('id', 'sensor', 'moment')


