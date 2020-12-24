from fastapi import FastAPI, APIRouter
from bson import ObjectId
from typing import List, Optional
from app.database.model import client, Message, db
from app.database.controller import create_message,get_message
from app.database.message_model import MessageBody
from pydantic import BaseModel

database_api = APIRouter()


@database_api.get('/message/get')
async def list_message(channel_id:str,starttime:str,endtime:str):
    """
    Args: None 
    
    This route is used to get the messages from the database and is handled by a controller 
    get_message() from controller.py
    
    Return Type : List 
    
    """
    return get_message(channel_id,starttime,endtime)


@database_api.post('/message/post')
async def post_message(message: MessageBody):
    """[summary]
    This route is used to post the messages to the database and is handled by a controller 
    create_message() from controller.py
    
    Args:
        message (MessageBody): [This is a Base Model (MessageBody)]

    Returns:
        [List]: create_message(message.channel_id,message.content,message.sender_id)
    """
    return create_message(message.channel_id,message.content,message.sender_id)


