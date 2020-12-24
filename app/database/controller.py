from fastapi import FastAPI,APIRouter
from datetime import datetime
from typing import List, Optional
import dateutil.parser
import pymongo
from app.database.model import client, Message, db 
from app.database.message_model import MessageBody
from app.database.settings import DB_NAME,COLLECTION_NAME
from app.database.mongo import close_mongo_connection, connect_to_mongo, get_nosql_db, AsyncIOMotorClient
from bson import ObjectId 
import logging
import datetime 
from tzlocal import get_localzone 

database_api = APIRouter()

async def get_message(channel_id:str,starttime:str,endtime:str):
    """[summary]
    The Function is used to fetch all the data in the DB for a specific channel
    Args:
        channel_id (str): Channel_UUID
        starttime (str): Time
        endtime (str): Time

    Returns:
        [List]: {cynergy}
    """
    try:
        COLLECTION_NAME = channel_id
        starttime = dateutil.parser.parse(starttime)
        endtime = dateutil.parser.parse(endtime)
        cynergy = []
        for i in db.COLLECTION_NAME.find({"channel_id":channel_id,'$and':[{'timestamp': { '$gte' : starttime },'timestamp': { '$lt' : endtime }}]}):
            await cynergy.append(Message(**i))
            print(i)
        return {'The Message Data is ': cynergy}
    except pymongo.errors.CollectionInvalid as e:
        logging.info(e)
        pass

async def create_message(channel_id:str,content:str,sender_id:str):
    """[summary]
    The Function is used to create only one message and insert the data into DB 
    
    Args:
        channel_id (str): Channel_UUID
        content (str): Message
        sender_id (str): User_ID
        timestamp (str): Time

    Returns:
        [List]: {"channel_id":channel_id,"content":content,"sender_id":sender_id,"timestamp":timestamp}
    """
    try:
        timestamp = datetime.datetime.now()
        ret = db.COLLECTION_NAME.insert_one({"channel_id":channel_id,"content":content,"sender_id":sender_id,"timestamp":timestamp})
        print(ret)
        return {"channel_id":channel_id,"content":content,"sender_id":sender_id,"timestamp":timestamp}
    except pymongo.errors.CollectionInvalid as e:
        logging.info(e)
        pass



