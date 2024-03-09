from channels.generic.websocket import AsyncWebsocketConsumer
from channels.db import database_sync_to_async
import json

from accounts.models import CustomUser
from .models import Message


class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        current_user_id = self.scope['user'].id
        other_user_id = int(self.scope['url_route']['kwargs']['other_user_id'])
        self.room_name = f'chat_{current_user_id * other_user_id}'
        self.room_group_name = self.room_name

        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        await self.accept()

        previous_messages = await self.get_previous_messages()

        await self.send_previous_messages(previous_messages)

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    async def receive(self, text_data):
        sender_id = self.scope['user'].id
        sender = await self.get_user(sender_id)
        text_data_json = json.loads(text_data)
        message_content = text_data_json['message']

        message = await self.create_message(
            room_name=self.room_name,
            sender=sender,
            content=message_content
        )

        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': message.content,
                'sender_id': message.sender.id,
                'timestamp': str(message.timestamp)
            }
        )

    async def chat_message(self, event):
        message = event['message']
        sender_id = event['sender_id']
        timestamp = event['timestamp']

        await self.send(text_data=json.dumps({
            'message': message,
            'sender_id': sender_id,
            'timestamp': timestamp
        }))

    async def send_previous_messages(self, messages_data):
        await self.send(text_data=json.dumps({
            'previous_messages': messages_data
        }))

    @database_sync_to_async
    def get_user(self, user_id):
        return CustomUser.objects.get(id=user_id)

    @database_sync_to_async
    def create_message(self, room_name, sender, content):
        return Message.objects.create(
            room_name=room_name,
            sender=sender,
            content=content
        )

    @database_sync_to_async
    def get_previous_messages(self):
        previous_messages =  Message.objects.filter(room_name=self.room_name)
        messages_data = []

        for message in previous_messages:
            messages_data.append({
                'message': message.content,
                'sender_id': message.sender.id,
                'timestamp': str(message.timestamp)
            })

        return messages_data