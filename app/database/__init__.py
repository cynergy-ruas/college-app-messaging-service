import os

from dotenv import find_dotenv, load_dotenv

from app.config import COLLECTION_NAME, DB_NAME, MONGO_URL
from pymongo import MongoClient


load_dotenv(find_dotenv())


class MongoDB:
    """
    This Class is used the Handle all the Settings for MongoDB Stuff
    """

    _instance = None

    def __init__(self):
        self.client = MongoClient(MONGO_URL)
        self.db = self.client[DB_NAME]

    @staticmethod
    def get_instance():
        """
        This Function is used to get the instance of the MongoDB Class
        Returns:
            This Returns the object of the MongoDB Class
        """
        if MongoDB._instance is None:
            MongoDB._instance = MongoDB()
        return MongoDB._instance

    @staticmethod
    def get_database():
        """
        This Function is used to get the database
        Returns:
             This Returns the Database
        """
        return MongoDB.get_instance().db

    @staticmethod
    def get_collection():
        """
        This Function is used to get the collection
        Returns:
             This Returns the collection
        """

        return MongoDB.get_database()[COLLECTION_NAME]
