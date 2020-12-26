import json
from collections import defaultdict

from app.database.database_queries import create_message
from fastapi import WebSocket


class Notifier:
    """
    This Class Manages all the sessions and members with message routing:
    """

    def __init__(self):
        self.connections: dict = defaultdict(dict)
        self.generator = self.get_notification_generator()

    async def get_notification_generator(self):
        """
        This Function basically yields the incoming messages and notify.
        """
        while True:
            message = yield
            msg = message["message"]
            channel_id = message["channel_id"]
            sender_id = message["sender_id"]
            await self._notify(msg, channel_id, sender_id)

    async def push(self, msg: str, channel_id: str = None, sender_id: str = None):
        """
        This Function is used to send the data throught websockets and also store it in DB
        Args:
            msg (str): The actual message
            channel_id (str, optional): The Channel UUID
            sender_id (str, optional): The Sender ID
        """
        message_body = {
            "message": msg,
            "channel_id": channel_id,
            "sender_id": sender_id,
        }
        await create_message(channel_id, msg, sender_id)
        await self.generator.asend(message_body)

    async def connect(self, websocket: WebSocket, channel_id: str):
        """
        This function is used to accept the web socket connection and append \
        it to the list for the specific channel:
        Args:
            websocket (WebSocket)
            channel_id (str): This is Channel ID
        """
        await websocket.accept()
        if self.connections[channel_id] == {} or len(self.connections[channel_id]) == 0:
            self.connections[channel_id] = []
        self.connections[channel_id].append(websocket)

    def remove(self, websocket: WebSocket, channel_id: str):
        """
        This function is used to remove the connection of the websockets for the specific channel:
        Args:
            websocket (WebSocket)
            channel_id (str): This is Channel ID
        """
        self.connections[channel_id].remove(websocket)

    async def _notify(self, message: str, channel_id: str, sender_id: str):
        """
        This function is being used to know the live connections and allows to send messages:
        Args:
            message (str): The Message that you actually send through the socket
            channel_id (str): This is Channel ID
            sender_id (str): This is Sender ID
        """
        living_connections = []
        while len(self.connections[channel_id]) > 0:
            websocket = self.connections[channel_id].pop()
            response = json.dumps({"message": message, "sender_id": sender_id})
            await websocket.send_text(response)
            living_connections.append(websocket)
        self.connections[channel_id] = living_connections
