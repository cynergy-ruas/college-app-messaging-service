import os
MONGO_URL = os.environ.get("MONGODB_URI")
DB_NAME = "message"
COLLECTION_NAME = "messages"