"""
ASGI config for structured project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/6.0/howto/deployment/asgi/
"""
import os

from django.core.asgi import get_asgi_application

from channels.routing import ProtocolTypeRouter, URLRouter

from noti.routing import websocket_urlpatterns
from notifications.middleware import JWTAuthMiddleware

os.environ.setdefault(
    "DJANGO_SETTINGS_MODULE",
    "structured.settings"
)

application=ProtocolTypeRouter({
    'http':get_asgi_application(),
    'websocket':URLRouter(websocket_urlpatterns)
    
})


