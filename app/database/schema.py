from bson import ObjectId
from typing import List, Optional
from fastapi import FastAPI
from pydantic import BaseModel, Field
from pymongo import MongoClient
import app.database.settings 
from unicodedata import name
# Connection Stuff 
client = MongoClient(app.database.settings.MONGO_URL) 
db = client[app.database.settings.DB_NAME]

# Using FastAPI
app = FastAPI()

class PyObjectId(ObjectId):
    """
    This is Class is Used to Verify the database just like a custom validator 
    """
    @classmethod
    def __get_validators__(cls):
        yield cls.validate
    @classmethod
    def validate(cls, v):
        if not ObjectId.is_valid(v):
            raise ValueError('Invalid objectid')
        return ObjectId(v)
    @classmethod
    def __modify_schema__(cls, field_schema):
        field_schema.update(type='string')


#creating channel class to store schema 
class Message(BaseModel):
    """
     This Class is the Schema for our data model 
    
     Schema :
        \n_id -> Object ID,
        \nName -> String,
        \nMessage -> String,
    
     Updated Schema for next week:
    
        0. Object_id
        1. sender_id
        2. channel_id
        3.message_body
        4.time_stamp
    
    """
    id: Optional[PyObjectId] = Field(alias='_id')
    Name: str
    Message: str  

    class Config:
        """
        This Class converts Object ID into String 
        """
        arbitrary_types_allowed = True
        json_encoders = {
            ObjectId: str
        }
        
        
        