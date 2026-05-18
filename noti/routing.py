from django.urls import path
from .import consumer
websocket_urlpatterns=[
    path("ws/asc/",consumer.AsynchronusConsumer.as_asgi()),
    path("ws/sc/",consumer.SynchronusConsumer.as_asgi()),

]