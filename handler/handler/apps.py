from django.apps import AppConfig


class HandlerConfig(AppConfig):
    name = 'handler'

    def ready(self):
        import handler.handlers