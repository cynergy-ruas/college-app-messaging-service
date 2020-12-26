import datetime
import logging
from datetime import datetime

import app.database.database_queries as mongo_queries
import dateutil.parser
import pymongo
from app.utils.errors import APIErrors
from dateutil.parser import ParserError
from fastapi import APIRouter

database_api = APIRouter()


async def get_message(channel_id: str, start_time: str, end_time: str):
    """
    The Function is used to fetch all the massages in the DB for a specific channel
    Args:
        channel_id (str): Channel_UUID
        starttime (str): The start time to fetch messages
        endtime (str): The end time to fetch messages
 
    Raise: If the channel is not found then 404 exception \
        if the time format is incorrect then 422 exeception \
        if there is a Mongo Execption then monog exception


    Returns:
        [List]: A List of all the messages from the channel between two times
    """
    try:
        start_time = dateutil.parser.parse(start_time)
        end_time = dateutil.parser.parse(end_time)
        if not mongo_queries.check_channel_exists(channel_id):
            raise APIErrors(404, "The channel you are looking for doesn't exist")
        return mongo_queries.get_message_between(channel_id, start_time, end_time)
    except pymongo.errors.CollectionInvalid as e:
        logging.info(e)
    except ParserError as e:
        raise APIErrors(422, "Invalid Time Format.")


async def create_message(channel_id: str, content: str, sender_id: str):
    """
    The Function is used to create only one message and insert the data into DB

    Args:
        channel_id (str): Channel_UUID
        content (str): Message
        sender_id (str): User_ID
        timestamp (str): Time

    Raise: Mongo Execption

    Returns:
        [List]: Returns a list of data inserted
    """
    try:
        timestamp = datetime.datetime.now()
        mongo_queries.create_message(channel_id, content, sender_id, timestamp)
        return {
            "channel_id": channel_id,
            "content": content,
            "sender_id": sender_id,
            "timestamp": timestamp,
        }
    except pymongo.errors.CollectionInvalid as e:
        logging.info(e)
        pass
