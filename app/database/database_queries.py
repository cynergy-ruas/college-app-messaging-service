from datetime import datetime

from app.database import MongoDB


def get_message_between(channel_id: str, start_time: datetime, end_time: datetime):
    """
    This Function is used to get the Mongo Query for receiving the messages between a certion start and end time
    Args:
        channel_id (str): The Channel UUID
        start_time (datetime): The start time to fetch messages
        end_time (datatime): The end time to fetch messages

    Returns:
        List : List of the Mongo Query
    """
    return list(
        MongoDB.get_collection().find(
            {
                "channel_id": channel_id,
                "$and": [
                    {"timestamp": {"$gte": start_time}, "timestamp": {"$lt": end_time}}
                ],
            }
        )
    )


async def create_message(channel_id: str, content: str, sender_id: str):
    """[summary]
    This Function is used to create a message using Mongo Query :
        channel_id (str): The Channel UUID
        content (str): The Message :
        sender_id (str): The Sender UUID
        timestamp (datetime): Timestamp
    """
    timestamp = datetime.now()
    MongoDB.get_collection().insert_one(
        {
            "channel_id": channel_id,
            "content": content,
            "sender_id": sender_id,
            "timestamp": timestamp,
        }
    )


def check_channel_exists(channel_id: str):
    """
    This function is used to check if the channel exists in DB or not
    Args:
        channel_id (str):  The Channel UUID

    Returns:
        Boolean: Returns a bool value if the collection is found or not
    """
    return bool(MongoDB.get_collection().find_one({"channel_id": channel_id}))
