from datetime import datetime

from bson import ObjectId
from fastapi import FastAPI
from pydantic import BaseModel, Field


class PyObjectId(ObjectId):
    """
    This is Class is Used to Verify the database just like a custom validator:
    """

    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def validate(cls, _v):
        if not ObjectId.is_valid(_v):
            raise ValueError("Invalid objectid")
        return ObjectId(_v)

    @classmethod
    def __modify_schema__(cls, field_schema):
        field_schema.update(type="string")


class Message(BaseModel):
    """
    This is the Base Model of the database:
    Args:
        BaseModel : FASTAPI Base Model:
    """

    _id: PyObjectId = Field(alias="_id")
    channel_id: str
    content: str
    sender_id: str
    timestamp: datetime = None

    class Config:
        """
        This Class converts Object ID into String:
        """

        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}
