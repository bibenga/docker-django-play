import logging

from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer
from channels.layers import get_channel_layer
from django.contrib.admin.models import LogEntry
from django.contrib.auth import user_logged_in
from django.db.models.signals import post_save
from django.dispatch import receiver

from handler.middleware import get_current_user

_l = logging.getLogger(__name__)


class AdminConsumer(WebsocketConsumer):
    def connect(self):
        user = self.scope.get('user')
        _l.info('AdminConsumer.connect: user=%s, channel_name=%s', user, self.channel_name)
        if user and user.is_active and (user.is_superuser or user.is_staff):
            async_to_sync(self.channel_layer.group_add)('admin', self.channel_name)
            self.accept()
        else:
            self.close(code='permission denied')

    def disconnect(self, close_code):
        user = self.scope.get('user')
        _l.info('AdminConsumer.disconnect: user=%s, channel_name=%s, close_code=%s', user, self.channel_name,
                close_code)
        async_to_sync(self.channel_layer.group_discard)('admin', self.channel_name)

    def receive(self, text_data=None, bytes_data=None):
        pass

    def admin_user_logged_in(self, event):
        _l.info('AdminConsumer.admin_user_logged_in: %s', event)
        self.send(text_data=event['text'])

    def admin_operation(self, event):
        _l.info('AdminConsumer.admin_operation: %s', event)
        user = self.scope["user"]
        if getattr(user, 'id', None) != event['user']:
            self.send(text_data=event['text'])


@receiver(user_logged_in, dispatch_uid='admin_user_logged_in')
def admin_user_logged_in(sender, request, user, **kwargs):
    if user.is_superuser or user.is_staff:
        msg = {
            "type": "admin.user_logged_in",
            "user": user.id,
            "text": f"{user} logged in",
        }
        channel_layer = get_channel_layer()
        async_to_sync(channel_layer.group_send)("admin", msg)


@receiver(post_save, sender=LogEntry, dispatch_uid='admin_operation')
def admin_operation(sender, instance=None, created=None, **kwargs):
    user = get_current_user()
    msg = {
        "type": "admin.operation",
        "user": user.id,
        "text": f"{user} - {instance.content_type}:{instance.id} - {instance}",
    }
    channel_layer = get_channel_layer()
    async_to_sync(channel_layer.group_send)("admin", msg)
