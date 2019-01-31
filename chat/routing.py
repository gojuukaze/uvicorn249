# -*- coding: utf-8 -*-
from django.conf.urls import url

from . import consumers

websocket_urlpatterns = [
    url(r'^ws/chat$', consumers.ChatConsumer),
    url(r'^ws/chat/async$', consumers.AsyncChatConsumer),
]
