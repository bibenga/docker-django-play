#!/bin/sh

export DJANGO_SETTINGS_MODULE=handler.settings.dev

celery -A micro worker -E -l debug -B --scheduler django_celery_beat.schedulers:DatabaseScheduler
