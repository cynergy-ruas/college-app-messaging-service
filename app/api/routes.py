from typing import List

from app.models.model import Message
from app.services.message_service import get_message
from app.utils.errors import APIErrors
from fastapi import APIRouter, HTTPException

database_api = APIRouter()


@database_api.get("/message/get", response_model=List[Message])
async def list_message(channel_id: str, start_time: str, end_time: str):
    """
    This route is used to get the messages from the database and is handled by a controller
    get_message() from message_service.py

    Args:
        channel_id (str): The channel UUID
        start_time (str): The start time
        end_time (str): The end time

    Returns:
        [List]: A List of all the messages from the channel between two times
    """
    try:
        return await get_message(channel_id, start_time, end_time)
    except APIErrors as err:
        raise HTTPException(status_code=err.code, detail=err.message)
