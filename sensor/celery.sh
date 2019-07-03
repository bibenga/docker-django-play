#!/bin/sh

export DJANGO_SETTINGS_MODULE=micro.settings.dev

celery -A micro worker -E -P solo -l debug -B -s celerybeat-schedule
