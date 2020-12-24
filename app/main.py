from fastapi import FastAPI
from fastapi import APIRouter
from app.api.routes import database_api
from app.services.ws_controller import websoc
app = FastAPI()
app.include_router(database_api)
app.include_router(websoc)
