from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
from django.conf.urls import url

from handler.consumers.admin import AdminConsumer


ws_urlpatterns = [
    url(r'^api/ws/admin/$', AdminConsumer),
]

application = ProtocolTypeRouter({
    'websocket': AuthMiddlewareStack(
        URLRouter(
            ws_urlpatterns
        )
    ),
})
