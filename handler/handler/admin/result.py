from django.contrib import admin

from handler.models.result import Result


@admin.register(Result)
class ResultAdmin(admin.ModelAdmin):
    model = Result
    list_display = ('id', 'sensor', 'code', 'moment', 'value')
    date_hierarchy = 'moment'
    ordering = ('-moment',)
    list_filter = ('moment', 'sensor')
    search_fields = ('sensor',)
