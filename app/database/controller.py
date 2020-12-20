from fastapi import FastAPI,APIRouter
from datetime import datetime
import dateutil.parser
from app.database.schema import client, Message, db 
from app.database.body import Messagebody
from bson import ObjectId 
import datetime 
from tzlocal import get_localzone # $ pip install tzlocal


some_router = APIRouter()


def get_message(channel_id,starttime,endtime):
    """
    Args : None 
    
    The Function is used to fetch all the data in the DB 
    
    Return Type : List 
    {"channel_id":channel_id })
    """
    starttime = dateutil.parser.parse(starttime)
    endtime = dateutil.parser.parse(endtime)
    print(starttime)
    print(endtime)
    cynergy = []
    for i in db.message.find({"channel_id":channel_id,'$and':[{'timestamp': { '$gte' : starttime },'timestamp': { '$lt' : endtime }}]}):
      cynergy.append(Message(**i))
      print(i)
    return {'The Message Data is ': cynergy}


def create_message(channel_id:str,content:str,sender_id:str):
    """[summary]
    The Function is used to create only one message and insert the data into DB 
    Args:
        channel_id (str): [description]
        content (str): [description]
        sender_id (str): [description]
        timestamp (str): [description]

    Returns:
        [List]: [description]
    """
    timestamp = datetime.datetime.now()
    ret = db.message.insert_one({"channel_id":channel_id,"content":content,"sender_id":sender_id,"timestamp":timestamp})
    return {"channel_id":channel_id,"content":content,"sender_id":sender_id,"timestamp":timestamp}

# def remove_message(_id):
#     """
#     Args: 
#     \n _id -> String 
    
#     The Function is used to delete one data from DB
    
#     Return Type : String
    
#     """
#     oid = ObjectId(_id)
#     try:
#         db.message.delete_one({"_id":oid})
#         return "Sucessfull"
#     except Exception as err:
#         print(err)
        
