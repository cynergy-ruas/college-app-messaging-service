from motor.motor_asyncio import AsyncIOMotorClient
import logging
from app.database.settings import MONGO_URL, MAX_CONNECTIONS_COUNT, MIN_CONNECTIONS_COUNT

class MongoDB:
    """[summary]
   So this basically creates a new connection to a single MongoDB instance
    """
    client: AsyncIOMotorClient = None
    
db = MongoDB()

async def get_nosql_db() -> AsyncIOMotorClient:
    """[summary]
    Just a simple function to return the mongo client (^basically the URL but hasn't been declared yet)
    Returns:
        AsyncIOMotorClient: [db.client]
    """
    return db.client


async def connect_to_mongo():
    """[summary]
    This Function is used to connect to MONGO with a Pool Size and passing the MONGO URL
    """
    db.client = AsyncIOMotorClient(
        str(MONGO_URL), maxPoolSize=MAX_CONNECTIONS_COUNT, minPoolSize=MIN_CONNECTIONS_COUNT,
    )
    logging.info("Connected to Database")


async def close_mongo_connection():
    """[summary]
    Closing the MONGO Connection
    """
    db.client.close()