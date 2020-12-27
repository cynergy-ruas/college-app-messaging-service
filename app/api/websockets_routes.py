import json

from app.database.database_queries import create_message
from app.services.websockets_service import Notifier
from fastapi import APIRouter, Request, WebSocket
from fastapi.templating import Jinja2Templates
from starlette.websockets import WebSocketDisconnect

websoc = APIRouter()

templates = Jinja2Templates(directory="templates")

notifier = Notifier()


@websoc.on_event("startup")
async def startup_event():
    """
    This function trigers to send the messages through sockets :
    """
    await notifier.generator.asend(None)


@websoc.get("/{channel_id}/{sender_id}")
async def get(request: Request, channel_id:str, sender_id:str):
    """
    API End Point for conncetion to Web Socket with Front End
    Args:
        request (Request): Request 
        channel_id (str): This is Channel ID
        sender_id (str): This is Sender ID

    Returns:
        returns the response in HTML file with websockets in frontend :
    """
    return templates.TemplateResponse(
        "index.html",
        {"request": request, "channel_id": channel_id, "sender_id": sender_id},
    )


@websoc.websocket("/ws/{channel_id}/{sender_id}")
async def websocket_endpoint(websocket: WebSocket, channel_id:str)-> Request :
    """
    API End Point for creating a websocket connection to send and receive data:
    Args:
        websocket (WebSocket): Websockets
        channel_id (str): This is Channel ID
        sender_id (str): This is Sender ID
    """
    await notifier.connect(websocket, channel_id)
    try:
        while True:
            data = await websocket.receive_text()
            data = json.loads(data)
            await notifier.push(data["message"], data["channel_id"], data["sender_id"])
    except WebSocketDisconnect:
        notifier.remove(websocket, channel_id)
