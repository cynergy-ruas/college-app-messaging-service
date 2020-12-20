from fastapi import FastAPI, APIRouter
from bson import ObjectId
from app.database.schema import client, Message, db
from app.database.controller import create_message,get_message
from app.database.body import Messagebody
from pydantic import BaseModel

some_router = APIRouter()


@some_router.get('/message/get')
async def list_message(channel_id:str,starttime:str,endtime:str):
    """
    Args: None 
    
    This route is used to get the messages from the database and is handled by a controller 
    \n get_message() from controller.py
    
    Return Type : List 
    
    """
    return get_message(channel_id,starttime,endtime)




@some_router.post('/message/post')
async def post_message(message: Messagebody):
    """
    Args: 
    \n Name -> String
    \n Message -> String
    
    This route is used to post the messages to the database and is handled by a controller 
    \n create_message() from controller.py
    
    Return Type : List
    
    """
    return create_message(message.channel_id,message.content,message.sender_id)


@some_router.delete('/deletemessage')
async def delete_message(_id):
    """
    Args: 
    \n _id -> String 
    
    This route is used to delete the messages from the database and is handled by a controller 
    \n remove_message() from controller.py
    
    Return Type : String
    
    """
    return remove_message(_id)
