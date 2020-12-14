from fastapi import FastAPI
from fastapi import APIRouter
from app.database.routes import some_router
# from app.services.wsconfig import websocketapp
app = FastAPI()
app.include_router(some_router)
# app.include_router(websocketapp)

