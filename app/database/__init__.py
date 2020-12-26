import os

from dotenv import find_dotenv, load_dotenv
from pymongo import MongoClient

load_dotenv(find_dotenv())


class MongoDB:
    """
    This Class is used the Handle all the Settings for MongoDB Stuff

    """

    _instance = None

    def __init__(self):
        MONGO_URL = os.environ.get("MONGO_URL")
        DB_NAME = os.environ.get("DB_NAME")
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
        COLLECTION_NAME = os.environ.get("COLLECTION_NAME")
        return MongoDB.get_database()[COLLECTION_NAME]
