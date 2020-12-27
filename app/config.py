import os
from decouple import config
MONGO_URL = config('MONGO_URL')
DB_NAME = config('DB_NAME')
COLLECTION_NAME = config('COLLECTION_NAME')