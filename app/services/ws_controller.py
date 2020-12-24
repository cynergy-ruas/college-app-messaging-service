from fastapi import FastAPI, WebSocket, Request, Depends,APIRouter
from starlette.websockets import WebSocketDisconnect
from collections import defaultdict
import logging
import asyncio
import json
from fastapi.templating import Jinja2Templates
from app.database.mongo import close_mongo_connection,connect_to_mongo,get_nosql_db, AsyncIOMotorClient
from pydantic import BaseModel
from app.database.settings import DB_NAME
from app.database.controller import get_message,create_message
import pymongo

websoc = APIRouter()


templates = Jinja2Templates(directory="templates")


class Notifier:
    """[summary]
    This Class Manages all the sessions and members with message routing 
    """
    def __init__(self):
        self.connections: dict = defaultdict(dict)
        self.generator = self.get_notification_generator()

    async def get_notification_generator(self):
        """[summary]
        This Function basically yields the incoming messages and notify  
        """
        while True:
            message = yield
            print(f"MESSAGE : {message}")
            msg = message["message"]
            channel_id = message["channel_id"]
            sender_id=message["sender_id"]
            await self._notify(msg, channel_id,sender_id)


    async def push(self, msg: str, channel_id: str = None,sender_id: str=None):
        """[summary]
        This Function is used to send the data throught websockets and also store it in DB
        Args:
            msg (str): [The Actual Message]
            channel_id (str, optional): [The Channel UUID]. Defaults to None.
            sender_id (str, optional): [The Sender ID]. Defaults to None.
        """
        message_body = {"message": msg, "channel_id": channel_id,"sender_id":sender_id}
        await create_message(channel_id,msg,sender_id)
        await self.generator.asend(message_body)




    async def connect(self, websocket: WebSocket, channel_id: str):
        """[summary]
        This function is used to accept the web socket connection and append it to the list for the specific channel 
        Args:
            websocket (WebSocket)
            channel_id (str): [This is Channel ID]
        """
        await websocket.accept()
        if self.connections[channel_id] == {} or len(self.connections[channel_id]) == 0:
            self.connections[channel_id] = []
        self.connections[channel_id].append(websocket)
        print(f"CONNECTIONS : {self.connections[channel_id]}")




    def remove(self, websocket: WebSocket, channel_id: str):
        """[summary]
        This function is used to remove the connection of the websockets for the specific channel 
        Args:
            websocket (WebSocket): [description]
            channel_id (str): [description]
        """
        self.connections[channel_id].remove(websocket)


    async def _notify(self, message: str, channel_id: str,sender_id:str):
        """[summary]
        This function is being used to know the live connections and allows to send messages 
        Args:
            message (str): [The Message that you actually send through the socket]
            channel_id (str): [This is Channel ID]
            sender_id (str): [This is Sender ID]
        """
        living_connections = []
        while len(self.connections[channel_id]) > 0:
            websocket = self.connections[channel_id].pop()
            response=json.dumps({"message":message,"sender_id":sender_id})
            await websocket.send_text(response)
            living_connections.append(websocket)
        self.connections[channel_id] = living_connections

notifier = Notifier()

@websoc.on_event("startup")
async def startup_event():
    """[summary]
    This function trigers to send the messages through sockets 
    """
    await notifier.generator.asend(None)
    

notifier = Notifier()

@websoc.get("/{channel_id}/{sender_id}")
async def get(request: Request, channel_id, sender_id):
    """[summary]
    API End Point for conncetion to Web Socket with Front End
    Args:
        request (Request): [request]
        channel_id ([type]): [This is Channel ID]
        sender_id ([type]): [This is Sender ID]

    Returns:
        returns the response in HTML file with websockets in frontend 
    """
    return templates.TemplateResponse(
        "index.html", {"request": request, "channel_id": channel_id, "sender_id": sender_id}
    )


@websoc.websocket("/ws/{channel_id}/{sender_id}")
async def websocket_endpoint(websocket: WebSocket, channel_id, sender_id):
    """[summary]
    API End Point for creating a websocket connection to send and receive data 
    Args:
        websocket (WebSocket): [Websockets]
        channel_id ([type]): [This is Channel ID]
        sender_id ([type]): [This is Sender ID]
    """
    await notifier.connect(websocket, channel_id)
    try:
        while True:
            data = await websocket.receive_text()
            data=json.loads(data)
            await notifier.push(data['message'],data['channel_id'], data['sender_id'])
    except WebSocketDisconnect:
        notifier.remove(websocket, channel_id)





