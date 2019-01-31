# -*- coding: utf-8 -*-
import json
import logging
from channels.generic.websocket import WebsocketConsumer, AsyncWebsocketConsumer


class ChatConsumer(WebsocketConsumer):
    def connect(self):
        logging.info('connect')
        self.accept()

    def disconnect(self, close_code):
        logging.info('disconnect')

    def receive(self, text_data):
        logging.info('receive ' + text_data)

        self.send(text_data=json.dumps({
            'message': text_data
        }))


class AsyncChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        logging.info('connect')
        await self.accept()

    async def disconnect(self, close_code):
        logging.info('disconnect')

    async def receive(self, text_data):
        logging.info('receive ' + text_data)

        await self.send(text_data=json.dumps({
            'message': text_data
        }))
