from fastapi import FastAPI,APIRouter
from bson import ObjectId
from app.database.schema import client, Message, db
from app.database.controller import create_message, get_message,remove_message
from pydantic import BaseModel
some_router = APIRouter() 

@some_router.get('/findallmessage')
async def list_message()-> list:
    """
    Args: None 
    
    This route is used to get the messages from the database and is handled by a controller 
    \n get_message() from controller.py
    
    Return Type : List 
    
    """
    return get_message()
  

@some_router.post('/createmessage')
async def post_message(message:Message) -> List:
   """
    Args: 
    \n Name -> String
    \n Message -> String
    
    This route is used to post the messages to the database and is handled by a controller 
    \n create_message() from controller.py
    
    Return Type : List
    
    """
   return create_message(message.Name,message.Message)

@some_router.delete('/deletemessage')
async def delete_message(_id) -> str:
   """
    Args: 
    \n _id -> String 
    
    This route is used to delete the messages from the database and is handled by a controller 
    \n remove_message() from controller.py
    
    Return Type : String
    
    """
   return remove_message(_id)