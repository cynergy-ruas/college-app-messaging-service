from fastapi import FastAPI
from app.api.routes import database_api
from app.api.websockets_routes import websoc
app = FastAPI()
app.include_router(database_api)
app.include_router(websoc)
