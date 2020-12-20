
from bson import ObjectId
from datetime import datetime
from typing import List, Optional
from fastapi import FastAPI
from pydantic import BaseModel, Field
from pymongo import MongoClient
import app.database.settings 
from unicodedata import name
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

class Messagebody(BaseModel):
    """[summary]

    Args:
        BaseModel ([type]): [description]
    """
    channel_id: Optional[str] 
    content: Optional[str]  
    sender_id : Optional[str] 
    timestamp: Optional[datetime] = None

    class Config:
        """
        This Class converts Object ID into String 
        """
        arbitrary_types_allowed = True
        json_encoders = {
            ObjectId: str
        }
   